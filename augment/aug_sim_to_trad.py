from hanziconv import HanziConv

from .base_operation import BaseOperation
from .utils import is_chinese_character


class SimplifiedToTraditional(BaseOperation):
    """Transform simplified chinese to traditional chinese"""

    def __init__(self):
        super(SimplifiedToTraditional, self).__init__()

    def can_replace(self, s):
        return any(is_chinese_character(c) for c in s) and s != HanziConv.toTraditional(s)

    def transform(self, s):
        return HanziConv.toTraditional(s)
