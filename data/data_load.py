import os.path as osp

from torch.utils.data import DataLoader

from pytorch_pretrained import BertTokenizer
from utils.download import download_pretrained
from .dataset import TextDataset


def init_tokenizer(config):
    model_name = config['model_name']
    pretrained_model_path = osp.join('pretrained', model_name)
    if not osp.exists(pretrained_model_path):
        download_pretrained(model_name)

    tokenizer = BertTokenizer.from_pretrained(pretrained_model_path)
    return tokenizer


def train_dataloader(config):
    tokenizer = init_tokenizer(config)
    train_data = TextDataset(root=config['train_dir'], tokenizer=tokenizer)
    dataloader = DataLoader(train_data, batch_size=config['batch_size'],
                            shuffle=True, num_workers=8)
    return dataloader


def val_dataloader(config):
    tokenizer = init_tokenizer(config)
    train_data = TextDataset(root=config['val_dir'], tokenizer=tokenizer)
    dataloader = DataLoader(train_data, batch_size=config['batch_size'],
                            shuffle=True, num_workers=8)
    return dataloader


def test_dataloader(config):
    tokenizer = init_tokenizer(config)
    train_data = TextDataset(root=config['test_dir'], tokenizer=tokenizer)
    dataloader = DataLoader(train_data, batch_size=128,
                            shuffle=False, num_workers=8)
    return dataloader
