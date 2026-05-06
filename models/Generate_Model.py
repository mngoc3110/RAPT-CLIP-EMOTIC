from torch import nn
from models.Temporal_Model import *
from models.Prompt_Learner import *
from models.Text import class_descriptor_5_only_face, class_descriptor_caer_only_face
from models.Adapter import Adapter
from clip import clip
import copy
import itertools

class GenerateModel(nn.Module):
    """
    RAPT-CLIP Model with flexible multi-stream architecture.
    
    Controlled by args.streams (comma-separated):
      - "face,body,context" → 3-stream (default)
      - "body,context"      → 2-stream (ablation, no face)
      - "face,body"         → 2-stream (original RAER-style)
    
    Each active stream: image_encoder → [adapter] → temporal_net → 512D
    Fusion: concat(active_streams) → project_fc → 512D → cosine sim with text
    """
    def __init__(self, input_text, clip_model, args):
        super().__init__()
        self.args = args
        
        # Parse active streams
        self.active_streams = [s.strip() for s in getattr(args, 'streams', 'face,body,context').split(',')]
        self.num_active_streams = len(self.active_streams)
        print(f"=> Active streams: {self.active_streams} ({self.num_active_streams}-stream)")
        
        self.is_ensemble = any(isinstance(i, list) for i in input_text)
        
        if self.is_ensemble:
            self.num_classes = len(input_text)
            self.num_prompts_per_class = len(input_text[0])
            self.input_text = list(itertools.chain.from_iterable(input_text))
            print(f"=> Using Prompt Ensembling with {self.num_prompts_per_class} prompts per class.")
        else:
            self.input_text = input_text

        self.prompt_learner = PromptLearner(self.input_text, clip_model, args)
        self.tokenized_prompts = self.prompt_learner.tokenized_prompts
        self.text_encoder = TextEncoder(clip_model)
        self.dtype = clip_model.dtype
        self.image_encoder = clip_model.visual

        # Face Adapter (only if face stream is active)
        if 'face' in self.active_streams:
            self.face_adapter = Adapter(c_in=512, reduction=4)

        # For MI Loss
        if args.dataset == "RAER":
            hand_crafted_prompts = class_descriptor_5_only_face
        elif args.dataset == "CAER" or args.dataset == "CAER-S":
            hand_crafted_prompts = class_descriptor_caer_only_face
        elif args.dataset == "EMOTIC":
            from models.Text import class_descriptor_emotic
            hand_crafted_prompts = class_descriptor_emotic
        elif args.dataset == "CK+":
            from models.Text import class_descriptor_ckplus
            hand_crafted_prompts = class_descriptor_ckplus
        elif args.dataset == "DAiSEE":
            from models.Text import class_descriptor_daisee
            hand_crafted_prompts = class_descriptor_daisee
        else:
            from models.Text import class_descriptor_7_only_face
            hand_crafted_prompts = class_descriptor_7_only_face
            
        self.tokenized_hand_crafted_prompts = torch.cat([clip.tokenize(p) for p in hand_crafted_prompts])
        with torch.no_grad():
            embedding = clip_model.token_embedding(self.tokenized_hand_crafted_prompts).type(self.dtype)
        self.register_buffer("hand_crafted_prompt_embeddings", embedding)

        # ==================== Temporal Transformers (only for active streams) ====================
        temporal_kwargs = dict(num_patches=16, input_dim=512, depth=args.temporal_layers,
                               heads=8, mlp_dim=1024, dim_head=64)
        
        if 'face' in self.active_streams:
            self.temporal_net = Temporal_Transformer_AttnPool(**temporal_kwargs)
        if 'body' in self.active_streams:
            self.temporal_net_body = Temporal_Transformer_AttnPool(**temporal_kwargs)
        if 'context' in self.active_streams:
            self.temporal_net_context = Temporal_Transformer_AttnPool(**temporal_kwargs)
        
        self.clip_model_ = clip_model
        
        # Fusion: num_active_streams * 512 → 512
        fusion_dim = self.num_active_streams * 512
        self.project_fc = nn.Linear(fusion_dim, 512)
        print(f"=> Fusion: {fusion_dim}D → 512D (project_fc)")

        # MoCo Initialization
        if hasattr(args, 'use_moco') and args.use_moco:
            print(f"=> Initializing MoCoRank ({self.num_active_streams}-Stream)...")
            self.moco_dim = 512
            self.moco_k = args.moco_k
            self.moco_m = args.moco_m
            self.moco_t = args.moco_t

            self.image_encoder_m = copy.deepcopy(self.image_encoder)
            self.project_fc_m = copy.deepcopy(self.project_fc)
            
            if 'face' in self.active_streams:
                self.face_adapter_m = copy.deepcopy(self.face_adapter)
                self.temporal_net_m = copy.deepcopy(self.temporal_net)
                for param in self.face_adapter_m.parameters(): param.requires_grad = False
                for param in self.temporal_net_m.parameters(): param.requires_grad = False
            if 'body' in self.active_streams:
                self.temporal_net_body_m = copy.deepcopy(self.temporal_net_body)
                for param in self.temporal_net_body_m.parameters(): param.requires_grad = False
            if 'context' in self.active_streams:
                self.temporal_net_context_m = copy.deepcopy(self.temporal_net_context)
                for param in self.temporal_net_context_m.parameters(): param.requires_grad = False

            for param in self.image_encoder_m.parameters(): param.requires_grad = False
            for param in self.project_fc_m.parameters(): param.requires_grad = False

            self.register_buffer("queue", torch.randn(self.moco_dim, self.moco_k))
            self.queue = nn.functional.normalize(self.queue, dim=0)
            self.register_buffer("queue_ptr", torch.zeros(1, dtype=torch.long))

    @torch.no_grad()
    def _momentum_update_key_encoder(self):
        for param_q, param_k in zip(self.image_encoder.parameters(), self.image_encoder_m.parameters()):
            param_k.data = param_k.data * self.moco_m + param_q.data * (1. - self.moco_m)
        if 'face' in self.active_streams:
            for param_q, param_k in zip(self.face_adapter.parameters(), self.face_adapter_m.parameters()):
                param_k.data = param_k.data * self.moco_m + param_q.data * (1. - self.moco_m)
            for param_q, param_k in zip(self.temporal_net.parameters(), self.temporal_net_m.parameters()):
                param_k.data = param_k.data * self.moco_m + param_q.data * (1. - self.moco_m)
        if 'body' in self.active_streams:
            for param_q, param_k in zip(self.temporal_net_body.parameters(), self.temporal_net_body_m.parameters()):
                param_k.data = param_k.data * self.moco_m + param_q.data * (1. - self.moco_m)
        if 'context' in self.active_streams:
            for param_q, param_k in zip(self.temporal_net_context.parameters(), self.temporal_net_context_m.parameters()):
                param_k.data = param_k.data * self.moco_m + param_q.data * (1. - self.moco_m)
        for param_q, param_k in zip(self.project_fc.parameters(), self.project_fc_m.parameters()):
            param_k.data = param_k.data * self.moco_m + param_q.data * (1. - self.moco_m)

    @torch.no_grad()
    def _dequeue_and_enqueue(self, keys):
        batch_size = keys.shape[0]
        ptr = int(self.queue_ptr)
        if ptr + batch_size > self.moco_k:
             batch_size = self.moco_k - ptr
             keys = keys[:batch_size]
        self.queue[:, ptr:ptr + batch_size] = keys.T
        ptr = (ptr + batch_size) % self.moco_k
        self.queue_ptr[0] = ptr

    def _encode_stream(self, image, encoder, adapter=None, temporal_net=None, compute_dtype=None):
        """Encode a single visual stream: image_encoder → [adapter] → temporal_net → 512D."""
        n, t, c, h, w = image.shape
        x = image.contiguous().view(-1, c, h, w)
        x = encoder(x.type(compute_dtype))
        if adapter is not None:
            x = adapter(x)
        x = x.contiguous().view(n, t, -1)
        x = temporal_net(x)
        return x

    @torch.no_grad()
    def forward_momentum(self, image_face, image_body, image_context):
        features = []
        if 'face' in self.active_streams:
            features.append(self._encode_stream(
                image_face, self.image_encoder_m, self.face_adapter_m, self.temporal_net_m, self.dtype))
        if 'body' in self.active_streams:
            features.append(self._encode_stream(
                image_body, self.image_encoder_m, None, self.temporal_net_body_m, self.dtype))
        if 'context' in self.active_streams:
            features.append(self._encode_stream(
                image_context, self.image_encoder_m, None, self.temporal_net_context_m, self.dtype))
        
        video_features = torch.cat(features, dim=-1)
        video_features = self.project_fc_m(video_features)
        video_features = video_features / (video_features.norm(dim=-1, keepdim=True) + 1e-6)
        return video_features
        
    def forward(self, image_face, image_body, image_context):
        """
        Multi-stream forward pass. Only active streams are computed.
        
        Args:
            image_face:    (B, T, C, H, W) face crops
            image_body:    (B, T, C, H, W) body crops
            image_context: (B, T, C, H, W) full images (context)
        
        Note: All 3 inputs are always passed for API consistency.
              Inactive streams are simply ignored (not encoded).
        """
        ################# Visual Part #################
        compute_dtype = self.dtype
        if image_face.device.type == 'mps':
            compute_dtype = torch.float32

        features = []
        
        if 'face' in self.active_streams:
            features.append(self._encode_stream(
                image_face, self.image_encoder, self.face_adapter, self.temporal_net, compute_dtype))
        
        if 'body' in self.active_streams:
            features.append(self._encode_stream(
                image_body, self.image_encoder, None, self.temporal_net_body, compute_dtype))
        
        if 'context' in self.active_streams:
            features.append(self._encode_stream(
                image_context, self.image_encoder, None, self.temporal_net_context, compute_dtype))

        # Concat active streams → project to 512D
        video_features = torch.cat(features, dim=-1)
        video_features = self.project_fc(video_features)
        video_features = video_features / (video_features.norm(dim=-1, keepdim=True) + 1e-6)

        ################# Text Part ###################
        prompts = self.prompt_learner()
        tokenized_prompts = self.tokenized_prompts
        
        with torch.cuda.amp.autocast(enabled=False):
            text_features = self.text_encoder(prompts, tokenized_prompts)
            text_features = text_features.float()
            text_features = text_features / (text_features.norm(dim=-1, keepdim=True) + 1e-6)

        hand_crafted_prompts = self.hand_crafted_prompt_embeddings
        tokenized_hand_crafted_prompts = self.tokenized_hand_crafted_prompts.to(hand_crafted_prompts.device)
        
        with torch.cuda.amp.autocast(enabled=False):
            hand_crafted_text_features = self.text_encoder(hand_crafted_prompts, tokenized_hand_crafted_prompts)
            hand_crafted_text_features = hand_crafted_text_features.float()
            hand_crafted_text_features = hand_crafted_text_features / (hand_crafted_text_features.norm(dim=-1, keepdim=True) + 1e-6)

        ################# MoCo Updates ###################
        moco_logits = None
        if self.training and hasattr(self.args, 'use_moco') and self.args.use_moco:
            with torch.no_grad():
                self._momentum_update_key_encoder()
                k_video_features = self.forward_momentum(image_face, image_body, image_context)
            
            l_pos = torch.einsum('nc,nc->n', [video_features, k_video_features]).unsqueeze(-1)
            l_neg = torch.einsum('nc,ck->nk', [video_features, self.queue.clone().detach()])
            moco_logits = torch.cat([l_pos, l_neg], dim=1)
            moco_logits /= self.moco_t
            self._dequeue_and_enqueue(k_video_features)

        ################# Classification ###################
        if self.is_ensemble:
            text_features = text_features.view(self.num_classes, self.num_prompts_per_class, -1)
            text_features = text_features / (text_features.norm(dim=-1, keepdim=True) + 1e-6)
            logits = torch.einsum('bd,cpd->bcp', video_features, text_features)
            output = torch.mean(logits, dim=2) / self.args.temperature
        else:
            output = video_features @ text_features.t() / self.args.temperature

        return output, text_features, hand_crafted_text_features, moco_logits