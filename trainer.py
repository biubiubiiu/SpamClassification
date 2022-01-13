import logging
import os

import numpy as np
import torch
from sklearn import metrics
from torch import nn
from tqdm import tqdm

from pytorch_pretrained.optimization import BertAdam


class Trainer:
    def __init__(self):
        self.model = None
        self.config = None
        self.train_loader = None
        self.test_data = None

        self.optimizer = None
        self.criterion = None

        self.device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')

    def set_model(self, model):
        self.model = model.to(self.device)

    def set_config(self, config):
        self.config = config

    def set_data(self, train_loader, test_data):
        self.train_loader = train_loader
        self.test_data = test_data

    @property
    def work_dir(self):
        if self.config is None:
            raise AttributeError('use `set_config()` to initialize `config`')
        return self.config.get('work_dir', None)

    def build(self):
        if self.model is None:
            raise AttributeError('use `set_model()` to initialize `model`')
        if self.config is None:
            raise AttributeError('use `set_config()` to initialize `config`')
        if self.train_loader is None or self.test_data is None:
            raise AttributeError('use `set_data()` to initialize `data`')

        param_optimizer = list(self.model.named_parameters())
        no_decay = ['bias', 'LayerNorm.bias', 'LayerNorm.weight']
        optimizer_grouped_parameters = [
            {'params': [p for n, p in param_optimizer if not any(nd in n for nd in no_decay)], 'weight_decay': 0.01},
            {'params': [p for n, p in param_optimizer if any(nd in n for nd in no_decay)], 'weight_decay': 0.0}
        ]

        self.optimizer = BertAdam(
            optimizer_grouped_parameters,
            lr=self.config['base_lr'],
            warmup=self.config['warmup'],
            t_total=len(self.train_loader) * self.config['epochs']
        )

        self.criterion = nn.CrossEntropyLoss()

        logging.info('Trainer build success')

    def start(self):
        epochs = self.config['epochs']
        best_acc = -1
        for epoch in range(epochs):
            train_loss = self.train()
            eval_acc = self.evaluate()
            is_best = eval_acc > best_acc
            if is_best:
                best_acc = eval_acc
            self.save_model(epoch, is_best)
            logging.info('Epoch: {}, Train Loss: {}'.format(epoch, train_loss))
            logging.info('Epoch: {}, Eval Accuracy: {}'.format(epoch, eval_acc))

    def train(self):
        self.model.train()
        loss_all = 0.
        for i, (tokens, labels) in enumerate(tqdm(self.train_loader)):
            for idx, item in enumerate(tokens):
                tokens[idx] = item.to(self.device)
            labels = labels.to(self.device)

            outputs = self.model(tokens)
            loss = self.criterion(outputs, labels.reshape(-1))

            self.optimizer.zero_grad()
            loss.backward()
            self.optimizer.step()

            loss_all += loss.item()

        return loss_all

    def evaluate(self):
        self.model.eval()
        predict_all = np.array([], dtype=int)
        labels_all = np.array([], dtype=int)
        with torch.no_grad():
            for (tokens, labels) in self.test_data:
                for idx, item in enumerate(tokens):
                    tokens[idx] = item.to(self.device)

                outputs = self.model(tokens)

                labels = labels.numpy().reshape(-1)
                pred = torch.argmax(outputs, dim=1).cpu().numpy().reshape(-1)
                labels_all = np.append(labels_all, labels)
                predict_all = np.append(predict_all, pred)

        acc = metrics.accuracy_score(labels_all, predict_all)
        return acc

    def save_model(self, epoch, is_best):
        work_dir = self.work_dir
        os.makedirs(work_dir, exist_ok=True)

        torch.save(self.model.state_dict(), os.path.join(work_dir, f'model_epoch_{epoch}.pth'))
        if is_best:
            torch.save(self.model.state_dict(), os.path.join(work_dir, f'model_best.pth'))
