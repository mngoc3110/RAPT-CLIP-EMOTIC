# trainer.py
import logging
import torch
import numpy as np
from sklearn.metrics import confusion_matrix, average_precision_score
from tqdm import tqdm
import os
import copy
import torchvision
import sys

from utils.utils import AverageMeter, get_loss_weight
from utils.loss import SemanticLDLLoss, AsymmetricLoss


class ModelEMA:
    """Exponential Moving Average of model weights.
    Keeps a shadow copy of model weights averaged over training steps.
    This reduces noise and improves generalization, typically +1-3% mAP.
    
    Usage:
        ema = ModelEMA(model, decay=0.999)
        # After each optimizer.step():
        ema.update(model)
        # For evaluation:
        ema.apply_shadow(model)  # load averaged weights
        # ... evaluate ...
        ema.restore(model)       # restore original weights
    """
    def __init__(self, model, decay=0.999):
        self.decay = decay
        self.shadow = {}
        self.backup = {}
        for name, param in model.named_parameters():
            if param.requires_grad:
                self.shadow[name] = param.data.clone()

    @torch.no_grad()
    def update(self, model):
        for name, param in model.named_parameters():
            if param.requires_grad and name in self.shadow:
                self.shadow[name] = self.decay * self.shadow[name] + (1.0 - self.decay) * param.data

    def apply_shadow(self, model):
        """Load EMA weights into model (backup originals first)."""
        for name, param in model.named_parameters():
            if param.requires_grad and name in self.shadow:
                self.backup[name] = param.data.clone()
                param.data = self.shadow[name].clone()

    def restore(self, model):
        """Restore original (non-EMA) weights from backup."""
        for name, param in model.named_parameters():
            if name in self.backup:
                param.data = self.backup[name].clone()
        self.backup = {}

class Trainer:
    """A class that encapsulates the training and validation logic."""
    def __init__(self, model, criterion, optimizer, scheduler, device,log_txt_path, 
                 mi_criterion=None, lambda_mi=0, 
                 dc_criterion=None, lambda_dc=0,
                 mi_warmup=0, mi_ramp=0,
                 dc_warmup=0, dc_ramp=0, use_amp=False, grad_clip=1.0, mixup_alpha=0.0,
                 use_ldl=False, ldl_warmup=0, use_ema=False, ema_decay=0.999,
                 use_tta=False, class_names=None):
        self.model = model
        self.criterion = criterion
        self.optimizer = optimizer
        self.scheduler = scheduler
        self.device = device
        self.print_freq = 10 
        self.log_txt_path = log_txt_path
        self.mi_criterion = mi_criterion
        self.lambda_mi = lambda_mi
        self.dc_criterion = dc_criterion
        self.lambda_dc = lambda_dc
        self.mi_warmup = mi_warmup
        self.mi_ramp = mi_ramp
        self.dc_warmup = dc_warmup
        self.dc_ramp = dc_ramp
        self.use_amp = use_amp
        self.grad_clip = grad_clip
        self.mixup_alpha = mixup_alpha
        self.use_ldl = use_ldl
        self.ldl_warmup = ldl_warmup
        self.use_tta = use_tta
        self.class_names = class_names  # For per-class AP logging
        
        # Detect multi-label mode (BCEWithLogitsLoss or AsymmetricLoss both use sigmoid + mAP)
        self.is_multilabel = isinstance(criterion, (torch.nn.BCEWithLogitsLoss, AsymmetricLoss))
        print(f"DEBUG: Trainer initialized with multi_label={self.is_multilabel}, use_ldl={use_ldl}")
        
        # EMA (Exponential Moving Average)
        self.ema = None
        if use_ema:
            self.ema = ModelEMA(model, decay=ema_decay)
            print(f"DEBUG: EMA enabled with decay={ema_decay}")
        
        if self.use_amp:
            self.scaler = torch.cuda.amp.GradScaler()
        
        # Create directory for saving debug prediction images
        self.debug_predictions_path = 'debug_predictions'
        os.makedirs(self.debug_predictions_path, exist_ok=True)

    def _save_debug_image(self, tensor, prediction, target, epoch_str, batch_idx, img_idx):
        """Saves a single image tensor for debugging."""
        # Un-normalize the image
        mean = torch.tensor([0.48145466, 0.4578275, 0.40821073], device=tensor.device).view(3, 1, 1)
        std = torch.tensor([0.26862954, 0.26130258, 0.27577711], device=tensor.device).view(3, 1, 1)
        tensor = tensor * std + mean
        tensor = torch.clamp(tensor, 0, 1)

        # Create a directory for the current epoch if it doesn't exist
        epoch_debug_path = os.path.join(self.debug_predictions_path, f"epoch_{epoch_str}")
        os.makedirs(epoch_debug_path, exist_ok=True)
        
        # Construct filename
        # In multi-label, prediction and target are vectors or indices of top-1
        filename = f"batch_{batch_idx}_img_{img_idx}_pred_{prediction}_true_{target}.png"
        filepath = os.path.join(epoch_debug_path, filename)
        
        # Save the image
        torchvision.utils.save_image(tensor, filepath)

    def mixup_data(self, x1, x2, x3, y, alpha=1.0):
        '''Returns mixed inputs, pairs of targets, and lambda (3-stream)'''
        if alpha > 0:
            lam = np.random.beta(alpha, alpha)
        else:
            lam = 1

        batch_size = x1.size(0)
        index = torch.randperm(batch_size).to(self.device)

        mixed_x1 = lam * x1 + (1 - lam) * x1[index, :]
        mixed_x2 = lam * x2 + (1 - lam) * x2[index, :]
        mixed_x3 = lam * x3 + (1 - lam) * x3[index, :]
        return mixed_x1, mixed_x2, mixed_x3, y[index], lam

    def _run_one_epoch(self, loader, epoch_str, is_train=True):
        """Runs one epoch of training or validation."""
        if is_train:
            self.model.train()
            mode_str = "Train"
        else:
            self.model.eval()
            mode_str = "Valid"

        losses = AverageMeter('Loss', ':.4e')
        mi_losses = AverageMeter('MI Loss', ':.4e')
        dc_losses = AverageMeter('DC Loss', ':.4e')
        
        all_logits_list = []
        all_targets_list = []
        
        saved_images_count = 0

        # Print weights at the start of training epoch
        if is_train:
            mi_weight = get_loss_weight(int(epoch_str), self.mi_warmup, self.mi_ramp, self.lambda_mi)
            dc_weight = get_loss_weight(int(epoch_str), self.dc_warmup, self.dc_ramp, self.lambda_dc)
            
            weight_msg = f"--- Epoch {epoch_str}: MI={mi_weight:.4f}, DC={dc_weight:.4f} ---"
            print(weight_msg)
            with open(self.log_txt_path, 'a') as f:
                f.write(weight_msg + '\n')

        context = torch.enable_grad() if is_train else torch.no_grad()
        pbar = tqdm(loader, desc=f"{mode_str} Epoch {epoch_str}", file=sys.stdout)
        
        with context:
            for i, (images_face, images_body, images_context, target) in enumerate(pbar):
                images_face = images_face.to(self.device)
                images_body = images_body.to(self.device)
                images_context = images_context.to(self.device)
                target = target.to(self.device)
                
                # Apply Mixup (3-stream)
                if is_train and self.mixup_alpha > 0:
                    images_face, images_body, images_context, target_b, lam = self.mixup_data(
                        images_face, images_body, images_context, target, self.mixup_alpha)

                with torch.cuda.amp.autocast(enabled=self.use_amp):
                    # Forward pass (3-stream: face, body, context)
                    output, learnable_text_features, hand_crafted_text_features, _ = self.model(images_face, images_body, images_context)
                    
                    # For MI and DC losses, average the learnable_text_features if ensembling
                    processed_learnable_text_features = learnable_text_features
                    if hasattr(self.model, 'is_ensemble') and self.model.is_ensemble:
                        num_classes = self.model.num_classes
                        num_prompts_per_class = self.model.num_prompts_per_class
                        processed_learnable_text_features = learnable_text_features.view(num_classes, num_prompts_per_class, -1).mean(dim=1)

                    # Calculate loss
                    if is_train and self.mixup_alpha > 0:
                        classification_loss = lam * self.criterion(output, target) + (1 - lam) * self.criterion(output, target_b)
                    else:
                        classification_loss = self.criterion(output, target)
                    
                    loss = classification_loss

                    if is_train and self.mi_criterion is not None:
                        mi_weight = get_loss_weight(int(epoch_str), self.mi_warmup, self.mi_ramp, self.lambda_mi)
                        mi_loss = self.mi_criterion(processed_learnable_text_features, hand_crafted_text_features)
                        loss += mi_weight * mi_loss
                        mi_losses.update(mi_loss.item(), target.size(0))

                    if is_train and self.dc_criterion is not None:
                        dc_weight = get_loss_weight(int(epoch_str), self.dc_warmup, self.dc_ramp, self.lambda_dc)
                        dc_loss = self.dc_criterion(processed_learnable_text_features)
                        loss += dc_weight * dc_loss
                        dc_losses.update(dc_loss.item(), target.size(0))

                if is_train:
                    self.optimizer.zero_grad()
                    if self.use_amp:
                        self.scaler.scale(loss).backward()
                        if self.grad_clip > 0:
                            self.scaler.unscale_(self.optimizer)
                            torch.nn.utils.clip_grad_norm_(self.model.parameters(), self.grad_clip)
                        self.scaler.step(self.optimizer)
                        self.scaler.update()
                    else:
                        loss.backward()
                        if self.grad_clip > 0:
                            torch.nn.utils.clip_grad_norm_(self.model.parameters(), self.grad_clip)
                        self.optimizer.step()
                    
                    # Update EMA after each optimization step
                    if self.ema is not None:
                        self.ema.update(self.model)

                losses.update(loss.item(), target.size(0))
                all_logits_list.append(output.detach().cpu())
                all_targets_list.append(target.cpu())

                if not is_train and saved_images_count < 16:
                    # Save a few face images for debug
                    self._save_debug_image(images_face[0,0].cpu(), 0, 0, epoch_str, i, 0)
                    saved_images_count += 1
                
                pbar.set_postfix({'Loss': f"{losses.avg:.4f}"})
        
        # Calculate final metrics
        all_logits = torch.cat(all_logits_list).numpy()
        all_targets = torch.cat(all_targets_list).numpy()
        
        if self.is_multilabel:
            # Calculate Average Precision for each class
            aps = []
            valid_classes = []
            for c in range(all_targets.shape[1]):
                if np.sum(all_targets[:, c]) > 0:
                    ap = average_precision_score(all_targets[:, c], all_logits[:, c])
                    aps.append(ap)
                    valid_classes.append(c)
            mAP = np.mean(aps) * 100
            
            prefix = f"{mode_str} Epoch: [{epoch_str}]"
            logging.info(f"{prefix} * mAP: {mAP:.3f}")
            with open(self.log_txt_path, 'a') as f:
                f.write(f'Current mAP: {mAP:.3f}\n')
                # Log per-class AP for analysis (only during validation)
                if not is_train and self.class_names is not None:
                    f.write(f'Per-class AP:\n')
                    for idx, c in enumerate(valid_classes):
                        cname = self.class_names[c] if c < len(self.class_names) else f'class_{c}'
                        f.write(f'  {cname}: {aps[idx]*100:.2f}%\n')
                    # Log bottom-5 classes for focus
                    sorted_aps = sorted(zip(valid_classes, aps), key=lambda x: x[1])
                    f.write(f'Bottom-5 weakest classes:\n')
                    for c, ap in sorted_aps[:5]:
                        cname = self.class_names[c] if c < len(self.class_names) else f'class_{c}'
                        f.write(f'  {cname}: {ap*100:.2f}%\n')
            return mAP, mAP, losses.avg, None # Return mAP twice to match return signature
        else:
            # Single-label logic (for other datasets)
            all_preds = np.argmax(all_logits, axis=1)
            all_targets_idx = np.argmax(all_targets, axis=1) if all_targets.ndim > 1 else all_targets
            cm = confusion_matrix(all_targets_idx, all_preds)
            war = (np.sum(all_preds == all_targets_idx) / len(all_targets_idx)) * 100
            class_acc = cm.diagonal() / (cm.sum(axis=1) + 1e-6)
            uar = np.nanmean(class_acc) * 100
            return war, uar, losses.avg, cm
        
    def train_epoch(self, train_loader, epoch_num):
        return self._run_one_epoch(train_loader, str(epoch_num), is_train=True)
    
    def validate(self, val_loader, epoch_num_str="Final"):
        # If EMA is enabled, swap to EMA weights for validation
        if self.ema is not None:
            self.ema.apply_shadow(self.model)
        
        result = self._run_one_epoch(val_loader, epoch_num_str, is_train=False)
        
        # Restore original weights after validation
        if self.ema is not None:
            self.ema.restore(self.model)
        
        return result
    
    def validate_tta(self, val_loader, epoch_num_str="Final"):
        """Test-Time Augmentation: evaluate with original + horizontal flip, average logits.
        Gives ~1-2% mAP boost for free by using two views of each image."""
        if self.ema is not None:
            self.ema.apply_shadow(self.model)
        
        self.model.eval()
        all_logits_list = []
        all_targets_list = []
        
        with torch.no_grad():
            pbar = tqdm(val_loader, desc=f"TTA Eval {epoch_num_str}", file=sys.stdout)
            for i, (images_face, images_body, images_context, target) in enumerate(pbar):
                images_face = images_face.to(self.device)
                images_body = images_body.to(self.device)
                images_context = images_context.to(self.device)
                target = target.to(self.device)
                
                # Original forward (3-stream)
                with torch.cuda.amp.autocast(enabled=self.use_amp):
                    output1, _, _, _ = self.model(images_face, images_body, images_context)
                
                # Horizontal flip forward (3-stream)
                images_face_flip = torch.flip(images_face, dims=[-1])  # flip W dimension
                images_body_flip = torch.flip(images_body, dims=[-1])
                images_context_flip = torch.flip(images_context, dims=[-1])
                with torch.cuda.amp.autocast(enabled=self.use_amp):
                    output2, _, _, _ = self.model(images_face_flip, images_body_flip, images_context_flip)
                
                # Average logits
                output = (output1 + output2) / 2.0
                
                all_logits_list.append(output.detach().cpu())
                all_targets_list.append(target.cpu())
        
        if self.ema is not None:
            self.ema.restore(self.model)
        
        all_logits = torch.cat(all_logits_list).numpy()
        all_targets = torch.cat(all_targets_list).numpy()
        
        if self.is_multilabel:
            aps = []
            for c in range(all_targets.shape[1]):
                if np.sum(all_targets[:, c]) > 0:
                    ap = average_precision_score(all_targets[:, c], all_logits[:, c])
                    aps.append(ap)
            mAP = np.mean(aps) * 100
            
            logging.info(f"TTA Eval [{epoch_num_str}] * mAP: {mAP:.3f}")
            with open(self.log_txt_path, 'a') as f:
                f.write(f'TTA mAP: {mAP:.3f}\n')
            return mAP
        else:
            all_preds = np.argmax(all_logits, axis=1)
            all_targets_idx = np.argmax(all_targets, axis=1) if all_targets.ndim > 1 else all_targets
            uar = np.mean(all_preds == all_targets_idx) * 100
            return uar