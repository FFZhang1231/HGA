from torch.utils.data import DataLoader
from data_utils.dataset import TGIFQA

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--mode', type=str, default='train')
    parser.add_argument('--task', type=str, default='FrameQA')
    args = parser.parse_args()
    print(args)

    dataset = TGIFQA(
        dataset_name=args.mode,
        data_type=args.task,
        csv_dir='/data1/jp/Datasets/tgif-qa/data/dataset',
        vocab_dir='/data1/jp/Datasets/tgif-qa/data/Vocabulary',
        feat_dir='/data1/jp/Datasets/tgif-qa/data/feats')
    dataloader = DataLoader(dataset, batch_size=2)
    # for i, (resnet, c3d, video_len, question, question_len, answer,
    #         answer_type) in enumerate(dataloader):
    #     print(
    #         resnet.size(),
    #         c3d.size(), video_len,
    #         question.size(), question_len, answer, answer_type)
    #     # torch.Size([1, 80]) torch.Size([1]) torch.Size([1, 80, 2048]) torch.Size([1, 80, 4096]) torch.Size([1]) torch.Size([1]) torch.Size([1])

    for i, data in enumerate(dataloader):
        print(data[3])
        print('Data size', len(data), [d.dtype for d in data])
        for i in data:
            print(i.size(), end=' ')
        print('\n')
