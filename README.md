# HGA
Pytorch code of Reasoning with Heterogeneous Graph Alignment for Video Question Answering.

![HGA](HGA.png)

## Requirements
Python 3.6
Pytorch 1.1

## Data
- [TGIF-QA](https://github.com/YunseokJANG/tgif-qa). Please cite [Link](https://arxiv.org/abs/1704.04497).
- [MSVD-QA and MSRVTT-QA](https://github.com/xudejing/video-question-answering). Please cite [Link](https://dl.acm.org/doi/pdf/10.1145/3123266.3123427).
- Extracted feature of the two datasets is [Here](https://github.com/fanchenyou/HME-VideoQA). Please cite [Link](https://arxiv.org/abs/1904.04357).

## Pre-trained Model
We provide four pre-trained models of TGIF-QA dataset.
- Trans_80.95.pth
- FrameQA_54.99.pth
- Count_4.092.pth
- Action_75.5.pth

## Test
The model test is carried out by loading the above pre-trained models. We provide the pre-trained models that achieve similar performance reported in the paper.

|Task of TGIF-QA|Performance|
|---|---|
|Count|4.092|
|Action|75.5|
|Trans|80.95|
|FrameQA|54.99|

```
CUDA_VISIBLE_DEVICES=0 python main.py  --test --task Count --num_workers 2 --batch_size 64
```

## Train
We give a base example of the subtask Action on TGIF-QA dataset (removing training tricks). You can modify the parameters at will on the corresponding datasets.
Please note that we have not tested the performance of the base model.
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

