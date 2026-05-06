import scipy.io
import json
import os
import numpy as np
from collections import Counter

# Configuration
MAT_FILE = 'emotic_dataset/CVPR17_Annotations.mat'
OUTPUT_DIR = 'emotic_dataset'

EMOTIC_CLASSES = [
    'Affection', 'Anger', 'Annoyance', 'Anticipation', 'Aversion', 'Confidence', 'Disapproval', 
    'Disconnection', 'Disquietment', 'Doubt/Confusion', 'Embarrassment', 'Engagement', 'Esteem', 
    'Excitement', 'Fatigue', 'Fear', 'Happiness', 'Pain', 'Peace', 'Pleasure', 'Sadness', 
    'Sensitivity', 'Suffering', 'Surprise', 'Sympathy', 'Yearning'
]
CLASS_TO_IDX = {c: i for i, c in enumerate(EMOTIC_CLASSES)}

def convert():
    if not os.path.exists(MAT_FILE):
        print(f"Error: {MAT_FILE} not found.")
        return

    print(f"Loading {MAT_FILE}...")
    try:
        mat = scipy.io.loadmat(MAT_FILE)
    except Exception as e:
        print(f"Failed to load mat file: {e}")
        return

    splits = ['train', 'val', 'test']
    body_bboxes = {}
    
    overall_stats = Counter()

    for split in splits:
        if split not in mat:
            continue
            
        print(f"\n{'='*20} PROCESSING {split.upper()} (26 CLASSES MULTI-LABEL) {'='*20}")
        output_txt = os.path.join(OUTPUT_DIR, f'{split}.txt')
        output_bbox_txt = os.path.join(OUTPUT_DIR, f'{split}_bbox.txt')
        
        split_stats = Counter()
        kept_count = 0
        
        with open(output_txt, 'w') as f_out, open(output_bbox_txt, 'w') as f_bbox_out:
            data = mat[split][0]
            
            for img_entry in data:
                filename = img_entry['filename'][0]
                folder = img_entry['folder'][0]
                path = os.path.join(folder, filename)
                
                persons = img_entry['person'][0]
                
                for person in persons:
                    try:
                        cats_raw = person['annotations_categories'][0,0][0][0]
                        current_cats = [str(c[0]) for c in cats_raw]
                    except:
                        continue
                    
                    if len(current_cats) == 0:
                        continue
                    
                    # Create multi-hot vector
                    label_vector = [0] * len(EMOTIC_CLASSES)
                    for c in current_cats:
                        if c in CLASS_TO_IDX:
                            label_vector[CLASS_TO_IDX[c]] = 1
                            split_stats[c] += 1
                            overall_stats[c] += 1
                    
                    label_str = ",".join([str(x) for x in label_vector])
                    
                    bbox = person['body_bbox'][0]
                    bbox_list = [int(b) for b in bbox.flatten()]
                    
                    # Standard EMOTIC format: path multi_label_vector x1 y1 x2 y2
                    f_out.write(f"{path} {label_str}\n")
                    f_bbox_out.write(f"{path} {label_str} {bbox_list[0]} {bbox_list[1]} {bbox_list[2]} {bbox_list[3]}\n")
                    
                    body_bboxes[path] = bbox_list
                    kept_count += 1
            
            print(f"Total Kept: {kept_count}")
            print("-" * 30)
            print(f"{'Class':<20} | {'Count':<10}")
            print("-" * 30)
            for cls in EMOTIC_CLASSES:
                print(f"{cls:<20} | {split_stats[cls]:<10}")
            print("-" * 30)

    # Save Body Bbox JSON
    with open(os.path.join(OUTPUT_DIR, 'emotic_body_bboxes.json'), 'w') as f:
        json.dump(body_bboxes, f)
        
    print(f"\nUpdated files: train_bbox.txt, val_bbox.txt, test_bbox.txt, emotic_body_bboxes.json")

if __name__ == "__main__":
    convert()