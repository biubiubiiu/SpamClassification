import pypinyin

from .base_operation import BaseOperation
from .utils import is_chinese_character


class ToPinyin(BaseOperation):
    """Replace characters to its Pinyin"""

    def __init__(self, random_pick=True):
        super(ToPinyin, self).__init__()
        self.random_pick = random_pick

    def can_replace(self, s):
        return any(is_chinese_character(c) for c in s)

    def transform(self, s):
        chars = list(s)
        for i, c in enumerate(chars):
            chars[i] = pypinyin.lazy_pinyin(c)[0] if is_chinese_character(c) else c
        return ''.join(chars)
