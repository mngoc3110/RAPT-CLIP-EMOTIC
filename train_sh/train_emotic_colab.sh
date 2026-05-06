#!/bin/bash
# EMOTIC TRAINING — Colab Optimized (Copy to local + Train)
# Tự động copy dataset từ Google Drive sang local SSD với progress bar,
# sau đó chạy training với tất cả optimizations.

set -e  # Dừng nếu có lỗi

# ==================== PATHS ====================
DRIVE_ROOT="/content/drive/.shortcut-targets-by-id/1xnZKVkEGo4a31G5nJZuDZZPkEdebso2l/RAPT-CLIP-EMOTIC"
LOCAL_DATA="/content/emotic_dataset"
REPO_DIR="${DRIVE_ROOT}"  # hoặc đổi thành /content/RAPT-CLIP-EMOTIC nếu clone repo local

export PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True

# ==================== STEP 1: Copy Dataset ====================
echo "============================================"
echo "  STEP 1: Copying EMOTIC dataset to local"
echo "============================================"

if [ -d "${LOCAL_DATA}/cvpr_emotic" ]; then
    echo "✓ Dataset đã tồn tại tại ${LOCAL_DATA}, bỏ qua copy."
else
    echo "→ Đang copy dataset từ Google Drive sang local SSD..."
    echo "  (Chỉ chạy 1 lần, lần sau sẽ bỏ qua)"
    echo ""

    # Tạo thư mục
    mkdir -p "${LOCAL_DATA}"

    # Copy annotation files (nhỏ, nhanh)
    echo "[1/4] Copying annotation files..."
    for f in train_bbox.txt test_bbox.txt val_bbox.txt train.txt test.txt val.txt train_bbox_balanced.txt; do
        if [ -f "${DRIVE_ROOT}/emotic_dataset/${f}" ]; then
            cp "${DRIVE_ROOT}/emotic_dataset/${f}" "${LOCAL_DATA}/" 2>/dev/null && echo "  ✓ ${f}"
        fi
    done

    # Copy bounding box JSON files
    echo "[2/4] Copying bounding box files..."
    for f in emotic_body_bboxes.json emotic_face_bboxes.json emotic_face_bboxes_mtcnn.json; do
        if [ -f "${DRIVE_ROOT}/emotic_dataset/${f}" ]; then
            cp "${DRIVE_ROOT}/emotic_dataset/${f}" "${LOCAL_DATA}/" 2>/dev/null && echo "  ✓ ${f}"
        fi
    done

    # Copy MAT file if exists
    if [ -f "${DRIVE_ROOT}/emotic_dataset/CVPR17_Annotations.mat" ]; then
        echo "[3/4] Copying annotations MAT file..."
        cp "${DRIVE_ROOT}/emotic_dataset/CVPR17_Annotations.mat" "${LOCAL_DATA}/" && echo "  ✓ CVPR17_Annotations.mat"
    else
        echo "[3/4] No MAT file found, skipping."
    fi

    # Copy images with progress bar using rsync
    echo "[4/4] Copying image folders (this may take a few minutes)..."
    echo ""

    # Check if rsync is available (preferred for progress)
    if command -v rsync &> /dev/null; then
        rsync -ah --info=progress2 "${DRIVE_ROOT}/emotic_dataset/cvpr_emotic/" "${LOCAL_DATA}/cvpr_emotic/"
    else
        # Fallback: use cp with a simple counter
        echo "  rsync not available, using cp..."
        
        # Count total files first
        TOTAL_FILES=$(find "${DRIVE_ROOT}/emotic_dataset/cvpr_emotic" -type f | wc -l)
        echo "  Total files to copy: ${TOTAL_FILES}"
        
        # Copy with progress using python (available on Colab)
        python3 -c "
import os, shutil, sys

src = '${DRIVE_ROOT}/emotic_dataset/cvpr_emotic'
dst = '${LOCAL_DATA}/cvpr_emotic'
total = int('${TOTAL_FILES}')
copied = 0

for root, dirs, files in os.walk(src):
    rel = os.path.relpath(root, src)
    dst_dir = os.path.join(dst, rel)
    os.makedirs(dst_dir, exist_ok=True)
    for f in files:
        shutil.copy2(os.path.join(root, f), os.path.join(dst_dir, f))
        copied += 1
        if copied % 100 == 0 or copied == total:
            pct = copied * 100 // total
            bar = '█' * (pct // 2) + '░' * (50 - pct // 2)
            sys.stdout.write(f'\r  [{bar}] {pct}% ({copied}/{total} files)')
            sys.stdout.flush()
print()
print('  ✓ Image copy complete!')
"
    fi

    echo ""
    echo "✓ Dataset copied successfully to ${LOCAL_DATA}"
    
    # Verify
    LOCAL_COUNT=$(find "${LOCAL_DATA}/cvpr_emotic" -type f | wc -l)
    echo "  → ${LOCAL_COUNT} image files in local storage"
fi

echo ""

# ==================== STEP 2: Train ====================
echo "============================================"
echo "  STEP 2: Starting EMOTIC Training"
echo "============================================"
echo ""
echo "Config:"
echo "  - CLIP Normalization: ✓ (fixed in dataloader)"
echo "  - Temperature: 0.05"
echo "  - ASL: gamma_neg=2.0, gamma_pos=0.0, clip=0.05"
echo "  - Epochs: 50, Warmup: 5"
echo "  - Mixup: OFF"
echo "  - EMA: 0.999, TTA: ON"
echo ""

cd "${REPO_DIR}"

python main.py \
  --mode train \
  --exper-name EMOTIC-Optimized-v2 \
  --dataset EMOTIC \
  --gpu 0 \
  --workers 4 \
  --use-amp \
  --epochs 50 \
  --batch-size 32 \
  --optimizer AdamW \
  --lr 3e-5 \
  --lr-image-encoder 1e-6 \
  --lr-prompt-learner 2e-4 \
  --lr-adapter 3e-5 \
  --weight-decay 0.05 \
  --scheduler cosine \
  --warmup-epochs 5 \
  --temporal-layers 1 \
  --num-segments 1 \
  --duration 1 \
  --image-size 224 \
  --seed 42 \
  --print-freq 50 \
  --root-dir "${LOCAL_DATA}/cvpr_emotic" \
  --train-annotation "${LOCAL_DATA}/train_bbox.txt" \
  --val-annotation "${LOCAL_DATA}/test_bbox.txt" \
  --test-annotation "${LOCAL_DATA}/test_bbox.txt" \
  --clip-path ViT-B/16 \
  --bounding-box-face "${LOCAL_DATA}/emotic_face_bboxes_mtcnn.json" \
  --bounding-box-body "${LOCAL_DATA}/emotic_body_bboxes.json" \
  --text-type prompt_ensemble \
  --contexts-number 16 \
  --class-token-position end \
  --class-specific-contexts True \
  --load_and_tune_prompt_learner True \
  --use-asl \
  --asl-gamma-neg 2.0 \
  --asl-gamma-pos 0.0 \
  --asl-clip 0.05 \
  --use-ema \
  --ema-decay 0.999 \
  --use-tta \
  --lambda_dc 0.1 \
  --mi-warmup 5 \
  --dc-warmup 5 \
  --lambda_mi 0.05 \
  --label-smoothing 0.0 \
  --crop-body \
  --grad-clip 1.0 \
  --mixup-alpha 0.0 \
  --temperature 0.05

echo ""
echo "============================================"
echo "  ✓ Training Complete!"
echo "============================================"
