import random

import pypinyin

from .base_operation import BaseOperation
from .utils import is_chinese_character, first


class CharacterToPinyin(BaseOperation):
    """Replace single character to its Pinyin

    Args:
        random_pick (bool): if `True`, random pick one character to replace, else
            find the first character the can be replaced. Default: `True`

    Returns:
        The transformed text with one character replaced, or the original text if no
        transformation coule be done
    """

    def __init__(self, random_pick=True):
        super(CharacterToPinyin, self).__init__()
        self.random_pick = random_pick

    def __call__(self, s):
        assert isinstance(s, str), f'Input should be a string, but got {type(s)}'

        try:
            idxs = list(range(len(s)))
            if self.random_pick:
                random.shuffle(idxs)
            idx_to_replace = first(idxs, lambda idx: is_chinese_character(s[idx]))
            replaced_content = pypinyin.lazy_pinyin(s[idx_to_replace])[0]
            return s[:idx_to_replace] + replaced_content + s[idx_to_replace + 1:]
        except StopIteration:
            return s
