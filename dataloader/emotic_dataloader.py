import os
import glob
import cv2
import json
import numpy as np
import torch
from PIL import Image
from torch.utils import data
from torchvision import transforms

class EmoticDataset(data.Dataset):
    """
    EMOTIC 3-Stream Dataset.
    
    Returns 4 items per sample: (face, body, context, label)
      - face:    Cropped face region (from face_bboxes JSON or fallback top-1/3 of body bbox)
      - body:    Cropped body region (from body_bboxes JSON or inline bbox in annotation)
      - context: Full original image (scene context)
      - label:   Multi-hot 26-class vector
    """
    def __init__(self, root_dir, list_file, mode='train', image_size=224, num_classes=26, 
                 bounding_box_face=None, bounding_box_body=None):
        """
        Args:
            root_dir (str): Base path to the dataset images.
            list_file (str): Path to the annotation file (e.g., 'train_bbox.txt').
            mode (str): 'train', 'val', or 'test'.
            image_size (int): Size to resize images to.
            bounding_box_face (str): Path to JSON file containing face bounding boxes.
            bounding_box_body (str): Path to JSON file containing body bounding boxes.
        """
        self.root_dir = root_dir
        self.list_file = list_file
        self.mode = mode
        self.image_size = image_size
        self.num_classes = num_classes
        
        # Load body bounding boxes from JSON
        self.body_bboxes = {}
        if bounding_box_body and os.path.exists(bounding_box_body):
            try:
                with open(bounding_box_body, 'r') as f:
                    self.body_bboxes = json.load(f)
                print(f"Loaded {len(self.body_bboxes)} body bounding boxes from {bounding_box_body}")
            except Exception as e:
                print(f"Error loading body bounding box JSON: {e}")
                
        # Load face bounding boxes from JSON
        self.face_bboxes = {}
        if bounding_box_face and os.path.exists(bounding_box_face):
            try:
                with open(bounding_box_face, 'r') as f:
                    self.face_bboxes = json.load(f)
                print(f"Loaded {len(self.face_bboxes)} face bounding boxes from {bounding_box_face}")
            except Exception as e:
                print(f"Error loading face bounding box JSON: {e}")
        
        self.classes = [
            'Affection', 'Anger', 'Annoyance', 'Anticipation', 'Aversion', 'Confidence', 'Disapproval', 
            'Disconnection', 'Disquietment', 'Doubt/Confusion', 'Embarrassment', 'Engagement', 'Esteem', 
            'Excitement', 'Fatigue', 'Fear', 'Happiness', 'Pain', 'Peace', 'Pleasure', 'Sadness', 
            'Sensitivity', 'Suffering', 'Surprise', 'Sympathy', 'Yearning'
        ]
        
        self.samples = self._make_dataset()
        
        # ==================== Transforms ====================
        if mode == 'train':
            # Face: lighter augmentation (face is small, heavy distortion hurts)
            self.transform_face = transforms.Compose([
                transforms.RandomResizedCrop(image_size, scale=(0.7, 1.0)),
                transforms.RandomHorizontalFlip(),
                transforms.RandomApply([
                    transforms.ColorJitter(brightness=0.3, contrast=0.3, saturation=0.2, hue=0.05)
                ], p=0.5),
                transforms.ToTensor(),
                transforms.Normalize(mean=[0.48145466, 0.4578275, 0.40821073], std=[0.26862954, 0.26130258, 0.27577711]),
                transforms.RandomErasing(p=0.15, scale=(0.02, 0.15), ratio=(0.3, 3.3)),
            ])
            # Body: moderate augmentation
            self.transform_body = transforms.Compose([
                transforms.RandomResizedCrop(image_size, scale=(0.5, 1.0)),
                transforms.RandomHorizontalFlip(),
                transforms.RandomApply([
                    transforms.ColorJitter(brightness=0.4, contrast=0.4, saturation=0.2, hue=0.1)
                ], p=0.8),
                transforms.RandomGrayscale(p=0.1),
                transforms.ToTensor(),
                transforms.Normalize(mean=[0.48145466, 0.4578275, 0.40821073], std=[0.26862954, 0.26130258, 0.27577711]),
                transforms.RandomErasing(p=0.25, scale=(0.02, 0.15), ratio=(0.3, 3.3)),
            ])
            # Context (Full Image): stronger augmentation for scene-level features
            self.transform_context = transforms.Compose([
                transforms.RandomResizedCrop(image_size, scale=(0.5, 1.0)),
                transforms.RandomHorizontalFlip(),
                transforms.RandomApply([
                    transforms.ColorJitter(brightness=0.4, contrast=0.4, saturation=0.4, hue=0.1)
                ], p=0.8),
                transforms.RandomGrayscale(p=0.2),
                transforms.ToTensor(),
                transforms.Normalize(mean=[0.48145466, 0.4578275, 0.40821073], std=[0.26862954, 0.26130258, 0.27577711]),
                transforms.RandomErasing(p=0.25, scale=(0.02, 0.2), ratio=(0.3, 3.3)),
            ])
        else:
            # Evaluation transforms (no augmentation)
            eval_transform = transforms.Compose([
                transforms.Resize((image_size, image_size)),
                transforms.ToTensor(),
                transforms.Normalize(mean=[0.48145466, 0.4578275, 0.40821073], std=[0.26862954, 0.26130258, 0.27577711]),
            ])
            self.transform_face = eval_transform
            self.transform_body = eval_transform
            self.transform_context = eval_transform

    def _make_dataset(self):
        samples = []
        if not os.path.exists(self.list_file):
            print(f"Error: Annotation file {self.list_file} not found.")
            return samples
            
        with open(self.list_file, 'r') as f:
            for line in f:
                parts = line.strip().split()
                if len(parts) >= 2:
                    rel_path = parts[0]
                    # Handle multi-label vector (comma separated)
                    label_str = parts[1]
                    if ',' in label_str:
                        label = [int(x) for x in label_str.split(',')]
                    else:
                        # Fallback for single label
                        label_idx = int(label_str)
                        label = [0] * self.num_classes
                        if 0 <= label_idx < self.num_classes:
                            label[label_idx] = 1
                    
                    full_path = os.path.join(self.root_dir, rel_path)
                    
                    # Parse inline bbox from annotation (if present)
                    bbox = None
                    if len(parts) >= 6:
                        try:
                            bbox = [int(float(x)) for x in parts[2:6]]
                        except ValueError:
                            pass 
                    
                    samples.append({'path': full_path, 'label': label, 'rel_path': rel_path, 'bbox': bbox})
        
        print(f"Loaded {len(samples)} samples from {self.list_file}")
        return samples

    def _crop_with_bbox(self, img, bbox, margin_scale=0.1):
        """Crop image using bounding box with optional margin expansion."""
        try:
            x1, y1, x2, y2 = bbox
            w, h = img.size
            
            bw = x2 - x1
            bh = y2 - y1
            x1 = max(0, x1 - bw * margin_scale)
            y1 = max(0, y1 - bh * margin_scale)
            x2 = min(w, x2 + bw * margin_scale)
            y2 = min(h, y2 + bh * margin_scale)
            
            cropped = img.crop((x1, y1, x2, y2))
            # Ensure crop is valid (non-zero size)
            if cropped.size[0] < 5 or cropped.size[1] < 5:
                return img
            return cropped
        except Exception:
            return img

    def _get_body_bbox(self, rel_path, bbox_txt):
        """Get body bounding box from inline annotation or JSON."""
        if bbox_txt is not None:
            return bbox_txt
        elif rel_path in self.body_bboxes:
            return self.body_bboxes[rel_path]
        return None

    def _get_face_bbox(self, rel_path, body_bbox=None):
        """Get face bounding box from JSON with spatial validation."""
        if rel_path in self.face_bboxes:
            face_bbox = self.face_bboxes[rel_path]
            # Spatial validation: Face center must be inside body bbox
            if body_bbox is not None and face_bbox is not None:
                fx1, fy1, fx2, fy2 = face_bbox
                bx1, by1, bx2, by2 = body_bbox
                fc_x = (fx1 + fx2) / 2
                fc_y = (fy1 + fy2) / 2
                if not (bx1 <= fc_x <= bx2 and by1 <= fc_y <= by2):
                    return None # Face belongs to someone else
            return face_bbox
        return None

    def __getitem__(self, index):
        sample = self.samples[index]
        path = sample['path']
        label = torch.tensor(sample['label'], dtype=torch.float32)
        rel_path = sample['rel_path']
        bbox_txt = sample['bbox']
        
        try:
            img = Image.open(path).convert('RGB')
        except Exception as e:
            print(f"Error loading {path}: {e}")
            img = Image.new('RGB', (self.image_size, self.image_size))

        # ==================== Context Stream (Full Image) ====================
        img_context = img

        # ==================== Body Stream (Body BBox crop) ====================
        body_bbox = self._get_body_bbox(rel_path, bbox_txt)
        if body_bbox is not None:
            img_body = self._crop_with_bbox(img, body_bbox, margin_scale=0.1)
        else:
            # Fallback: use full image if no body bbox available
            img_body = img

        # ==================== Face Stream (Face BBox crop) ====================
        face_bbox = self._get_face_bbox(rel_path, body_bbox)
        if face_bbox is not None:
            img_face = self._crop_with_bbox(img, face_bbox, margin_scale=0.2)
        else:
            # Fallback: use top 1/3 of body bbox as face approximation
            if body_bbox is not None:
                x1, y1, x2, y2 = body_bbox
                bh = y2 - y1
                fallback_face_box = [x1, y1, x2, y1 + int(float(bh) / 3.0)]
                img_face = self._crop_with_bbox(img, fallback_face_box, margin_scale=0.1)
            else:
                # Last resort: use full image
                img_face = img
        
        # ==================== Apply Transforms ====================
        t_face = self.transform_face(img_face)
        t_body = self.transform_body(img_body)
        t_context = self.transform_context(img_context)

        # Add temporal dimension (T=1 for image datasets)
        t_face = t_face.unsqueeze(0)
        t_body = t_body.unsqueeze(0)
        t_context = t_context.unsqueeze(0)
        
        return t_face, t_body, t_context, label

    def __len__(self):
        return len(self.samples)

def emotic_train_data_loader(root_dir, list_file, image_size, batch_size, num_workers=4, 
                              bounding_box_face=None, bounding_box_body=None):
    dataset = EmoticDataset(root_dir, list_file, mode='train', image_size=image_size, 
                            bounding_box_face=bounding_box_face, bounding_box_body=bounding_box_body)
    return torch.utils.data.DataLoader(dataset, batch_size=batch_size, shuffle=True, 
                                        num_workers=num_workers, pin_memory=False, drop_last=True)

def emotic_val_data_loader(root_dir, list_file, image_size, batch_size, num_workers=4, 
                            bounding_box_face=None, bounding_box_body=None):
    dataset = EmoticDataset(root_dir, list_file, mode='val', image_size=image_size, 
                            bounding_box_face=bounding_box_face, bounding_box_body=bounding_box_body)
    return torch.utils.data.DataLoader(dataset, batch_size=batch_size, shuffle=False, 
                                        num_workers=num_workers, pin_memory=False)

def emotic_test_data_loader(root_dir, list_file, image_size, batch_size, num_workers=4, 
                             bounding_box_face=None, bounding_box_body=None):
    dataset = EmoticDataset(root_dir, list_file, mode='test', image_size=image_size, 
                            bounding_box_face=bounding_box_face, bounding_box_body=bounding_box_body)
    return torch.utils.data.DataLoader(dataset, batch_size=batch_size, shuffle=False, 
                                        num_workers=num_workers, pin_memory=False)