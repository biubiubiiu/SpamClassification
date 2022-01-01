import argparse

import numpy as np
import toml
import torch

from data import train_dataloader, val_dataloader
from models import init_model
from trainer import Trainer
from utils import logger_setup


def parse_args():
    parser = argparse.ArgumentParser(description='Train a spam classifier')
    parser.add_argument('config', help='train config file path')
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()

    config = toml.load(args.config)

    logger_setup(config)

    if 'seed' in config:
        seed = config['seed']
        np.random.seed(seed)
        torch.manual_seed(seed)
        torch.cuda.manual_seed_all(seed)

    train_loader = train_dataloader(config)
    val_loader = val_dataloader(config)

    model = init_model(config)

    # ------------ Start ------------
    agent = Trainer()

    agent.set_model(model)
    agent.set_data(train_loader, val_loader)
    agent.set_config(config)

    agent.build()

    agent.start()
