#!/bin/bash
# EMOTIC TRAINING — 2-Stream Architecture (Face, Body)
# Target: Ablation Study (RAPT-CLIP v1 Baseline)

export PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True

python main.py \
  --mode train \
  --exper-name EMOTIC-2Stream-Ablation \
  --dataset EMOTIC \
  --streams face,body \
  --gpu 0 \
  --workers 0 \
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
  --root-dir emotic_dataset/cvpr_emotic \
  --train-annotation emotic_dataset/train_bbox.txt \
  --val-annotation emotic_dataset/test_bbox.txt \
  --test-annotation emotic_dataset/test_bbox.txt \
  --clip-path ViT-B/16 \
  --bounding-box-face emotic_dataset/emotic_face_bboxes_mtcnn.json \
  --bounding-box-body emotic_dataset/emotic_body_bboxes.json \
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
