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

## Cite

```
@inproceedings{jiang2020reasoning,
  title={Reasoning with Heterogeneous Graph Alignment for Video Question Answering},
  author={Jiang, Pin and Han, Yahong},
  booktitle={Proceedings of the AAAI Conference on Artificial Intelligence},
  year={2020}
}
```

