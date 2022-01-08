import random

from resources import dict_char_to_shape_closed
from .base_operation import BaseOperation
from .utils import first, is_chinese_character


class CharacterToShapeClosed(BaseOperation):
    """Replace single character to its shape-closed one

    Args:
        random_pick (bool): if `True`, random pick one character to replace, else
            find the first character the can be replaced. Default: `True`

    Returns:
        The transformed text with one character replaced, or the original text if no
        transformation coule be done
    """

    def __init__(self, random_pick=True):
        super(CharacterToShapeClosed, self).__init__()
        self.dict = dict_char_to_shape_closed()
        self.random_pick = random_pick

    def __call__(self, s):
        assert isinstance(s, str), f'Input should be a string, but got {type(s)}'

        try:
            idxs = list(range(len(s)))
            idxs = list(filter(lambda idx: is_chinese_character(s[idx]), idxs))  # filter non-chinese characters
            if self.random_pick:
                random.shuffle(idxs)
            idx_to_replace = first(idxs, lambda idx: s[idx] in self.dict)
            replaced_char = random.choice(self.dict[s[idx_to_replace]])
            return s[:idx_to_replace] + replaced_char + s[idx_to_replace + 1:]
        except StopIteration:
            return s
