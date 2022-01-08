from abc import ABCMeta


class BaseOperation(object, metaclass=ABCMeta):
    """Base class for augmentations

    All the operations should subclass it
    All subclasses should overwrite ``__call__``
    """

    def __init__(self):
        super(BaseOperation, self).__init__()

    def __call__(self, *args, **kwargs):
        pass
