from abc import ABCMeta, abstractmethod


class BaseOperation(object, metaclass=ABCMeta):
    """Base class for augmentations

    All the operations should subclass it
    All subclasses should overwrite ``can_replace`` and ``transform``
    """

    def __init__(self):
        super(BaseOperation, self).__init__()

    def __call__(self, s):
        assert isinstance(s, str), f'Input should be a string, but got {type(s)}'
        return self.transform(s)

    @abstractmethod
    def can_replace(self, s):
        """Rewrite this function in subclasses"""

    @abstractmethod
    def transform(self, s):
        """Rewrite this function in subclasses"""
