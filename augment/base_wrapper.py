from .base_operation import BaseOperation


class BaseWrapper(BaseOperation):

    def __init__(self, ops):
        super(BaseWrapper, self).__init__()

        if not isinstance(ops, BaseOperation):
            raise ValueError('ops should be subclass of BaseOperation')
        self.ops = ops

    def can_replace(self, s):
        return self.ops.can_replace(s)

    def transform(self, s):
        return self.ops.transform(s)
