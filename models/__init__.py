from .bert import Bert
from .bert_cnn import BertCNN
from .bert_rcnn import BertRCNN
from .bert_rnn import BertRNN
from .ernie import Ernie

MODELS = {
    'bert': Bert,
    'bert_cnn': BertCNN,
    'bert_rcnn': BertRCNN,
    'bert_rnn': BertRNN,
    'ernie': Ernie
}


def init_model(config):
    model_name = config['model_name']
    model = MODELS[model_name]
    return model(config)
