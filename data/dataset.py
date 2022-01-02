import os.path as osp

import torch
from torch.utils.data import Dataset
from tqdm import tqdm

from .metainfo import LABELS, FILENAMES


class TextDataset(Dataset):
    PAD, CLS = '[PAD]', '[CLS]'

    def __init__(self, root, tokenizer):
        super(TextDataset, self).__init__()

        self.tokenizer = tokenizer
        self.tokens = self._load(root)

    def _load(self, root, pad_size=32):
        contents = []
        for (filename, label) in zip(FILENAMES, LABELS):
            with open(osp.join(root, filename), 'r', encoding='UTF-8') as f:
                for line in tqdm(f, desc='Prepare data'):
                    content = line.strip()
                    if not content:  # blank
                        continue

                    tokens = [self.CLS] + self.tokenizer.tokenize(content)
                    token_ids = self.tokenizer.convert_tokens_to_ids(tokens)

                    length_to_pad = max(pad_size - len(token_ids), 0)
                    token_ids = (token_ids + [0] * length_to_pad)[:pad_size]
                    mask = ([1] * len(token_ids) + [0] * length_to_pad)[:pad_size]
                    seq_len = min(len(tokens), pad_size)

                    contents.append((token_ids, label, seq_len, mask))

        return contents

    def __len__(self):
        return len(self.tokens)

    def __getitem__(self, idx):
        data = self.tokens[idx]
        x = torch.LongTensor(data[0])
        y = torch.LongTensor([data[1]])  # label
        seq_len = torch.LongTensor([data[2]])
        mask = torch.LongTensor(data[3])
        return (x, seq_len, mask), y
