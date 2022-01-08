from torch import nn


class ComposedModel(nn.Module):
    def __init__(self, model4spam, model4ham):
        super(ComposedModel, self).__init__()
        self.model4spam = model4spam
        self.model4ham = model4ham

    def forward(self, x):
        spam_classification = self.model4spam(x)  # batch_size * num_classes
        ham_classification = self.model4ham(x)
        return (spam_classification + ham_classification) / 2
