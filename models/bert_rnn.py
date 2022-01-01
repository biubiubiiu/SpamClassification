from torch import nn

from pytorch_pretrained import BertModel


class BertRNN(nn.Module):

    def __init__(self, config):
        super(BertRNN, self).__init__()
        self.bert = BertModel.from_pretrained('pretrained/bert')
        for param in self.bert.parameters():
            param.requires_grad = True
        self.lstm = nn.LSTM(config['hidden_size'], config['hidden_size'], config['num_layers'],
                            bidirectional=True, batch_first=True, dropout=config['dropout'])
        self.dropout = nn.Dropout(config['dropout'])
        self.fc_rnn = nn.Linear(config['hidden_size'] * 2, config['num_classes'])

    def forward(self, x):
        context = x[0]
        mask = x[2]
        encoder_out, text_cls = self.bert(context, attention_mask=mask, output_all_encoded_layers=False)
        out, _ = self.lstm(encoder_out)
        out = self.dropout(out)
        out = self.fc_rnn(out[:, -1, :])  # 句子最后时刻的 hidden state
        return out
