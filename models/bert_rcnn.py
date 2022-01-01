import torch
import torch.nn.functional as F
from torch import nn

from pytorch_pretrained import BertModel


class BertRCNN(nn.Module):

    def __init__(self, config):
        super(BertRCNN, self).__init__()
        self.bert = BertModel.from_pretrained(config.bert_path)
        for param in self.bert.parameters():
            param.requires_grad = True
        self.lstm = nn.LSTM(config['hidden_size'], config['hidden_size'], config['num_layers'],
                            bidirectional=True, batch_first=True, dropout=config['dropout'])
        self.maxpool = nn.MaxPool1d(config['pad_size'])
        self.fc = nn.Linear(config['hidden_size'] * 2 + config['hidden_size'], config['num_classes'])

    def forward(self, x):
        context = x[0]
        mask = x[2]
        encoder_out, text_cls = self.bert(context, attention_mask=mask, output_all_encoded_layers=False)
        out, _ = self.lstm(encoder_out)
        out = torch.cat((encoder_out, out), 2)
        out = F.relu(out)
        out = out.permute(0, 2, 1)
        out = self.maxpool(out).squeeze()
        out = self.fc(out)
        return out
