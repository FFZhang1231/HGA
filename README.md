# HGA
![HGA](HGA.png)

## Data

## Pre-trained Model
We provide four pre-trained models for TGIF-QA dataset.

## Test
The model test is carried out by loading the above pre-trained models.
```
CUDA_VISIBLE_DEVICES=0 python main.py  --test --task Count --num_workers 2 --batch_size 64
```

## Train
```
CUDA_VISIBLE_DEVICES=0 python main.py --task Action --num_workers 2 --batch_size 64 --lr 0.0001 --model 7 --dropout 0.3 --change_lr none --ablation none
```
