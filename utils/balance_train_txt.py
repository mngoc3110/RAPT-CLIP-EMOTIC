import os
import random
from collections import defaultdict

input_file = 'emotic_dataset/train_bbox.txt'
output_file = 'emotic_dataset/train_bbox_balanced.txt'

# Configuration
# Target count for the majority class (Happy). 
# We set it slightly higher than the second largest class (Neutral ~600) to maintain variety but remove dominance.
TARGET_HAPPY_COUNT = 800 

def balance_dataset():
    if not os.path.exists(input_file):
        print(f"Error: {input_file} not found.")
        return

    # 1. Read all lines and group by label
    data_by_label = defaultdict(list)
    with open(input_file, 'r') as f:
        lines = f.readlines()

    for line in lines:
        parts = line.strip().split()
        if len(parts) < 2:
            continue
        label = int(parts[1])
        data_by_label[label].append(line)

    # 2. Process and Undersample
    final_lines = []
    print("Class Distribution (Before -> After):")
    
    # CAER Classes: 0:Anger, 1:Disgust, 2:Fear, 3:Happy, 4:Neutral, 5:Sad, 6:Surprise
    classes = sorted(data_by_label.keys())
    
    for cls in classes:
        lines_cls = data_by_label[cls]
        original_count = len(lines_cls)
        
        if cls == 3: # Happy
            # Shuffle to pick random samples
            random.seed(42) 
            random.shuffle(lines_cls)
            kept_lines = lines_cls[:TARGET_HAPPY_COUNT]
        else:
            # Keep all for minority classes
            kept_lines = lines_cls
            
        final_lines.extend(kept_lines)
        print(f"  Class {cls}: {original_count:>5} -> {len(kept_lines):>5}")

    # 3. Write to new file
    with open(output_file, 'w') as f:
        f.writelines(final_lines)

    print(f"\nTotal samples: {len(lines)} -> {len(final_lines)}")
    print(f"Saved balanced dataset to: {output_file}")

if __name__ == "__main__":
    balance_dataset()
