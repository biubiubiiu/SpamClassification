import argparse

import numpy as np
import toml
import torch
from sklearn import metrics
from tqdm import tqdm

from data import test_dataloader, CLASSES
from models import init_model


def parse_args():
    parser = argparse.ArgumentParser(description='Train a spam classifier')
    parser.add_argument('config', help='train config file path')
    parser.add_argument('checkpoint', help='checkpoint file')
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()

    config = toml.load(args.config)

    data_loader = test_dataloader(config)

    device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
    model = init_model(config).to(device)

    # test
    model.load_state_dict(torch.load(args.checkpoint))
    model.eval()

    predict_all = np.array([], dtype=int)
    labels_all = np.array([], dtype=int)
    with torch.no_grad():
        for (tokens, labels) in tqdm(data_loader):
            for idx, item in enumerate(tokens):
                tokens[idx] = item.to(device)
            labels = labels.to(device)

            outputs = model(tokens)

            labels = labels.cpu().numpy()[0]
            pred = torch.argmax(outputs, dim=1).cpu().numpy()[0]
            labels_all = np.append(labels_all, labels)
            predict_all = np.append(predict_all, pred)

    acc = metrics.accuracy_score(labels_all, predict_all)
    report = metrics.classification_report(labels_all, predict_all, target_names=CLASSES, digits=4)
    confusion = metrics.confusion_matrix(labels_all, predict_all)

    print('TTest Acc: {:>6.2%}'.format(acc))
    print('Precision, Recall and F1-Score...')
    print(report)
    print('Confusion Matrix...')
    print(confusion)
