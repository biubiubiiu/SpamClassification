from hanziconv import HanziConv
import random

from .utils import first, is_chinese_character
from .base_operation import BaseOperation


class SimplifiedToTraditional(BaseOperation):
    """Replace one simplified chinese character to traditional chinese

     Args:
        random_pick (bool): if `True`, random pick one character to replace, else
                find the first character the can be replaced. Default: `True`
    Returns:
        The transformed text with one character replaced, or the original text if no
        transformation coule be done
    """

    def __init__(self, random_pick=True):
        super(SimplifiedToTraditional, self).__init__()
        self.random_pick = random_pick

    def __call__(self, s):
        assert isinstance(s, str), f'Input should be a string, but got {type(s)}'

        try:
            idxs = list(range(len(s)))
            # filter non-simplified chinese characters
            idxs = list(filter(lambda idx: is_chinese_character(s[idx]), idxs))
            if self.random_pick:
                random.shuffle(idxs)

            # find one character that its traditional corresponding are different to itself
            idx_to_placed = first(idxs, lambda idx: s[idx] != HanziConv.toTraditional(s[idx]))
            replaced_char = HanziConv.toTraditional(s[idx_to_placed])
            return s[:idx_to_placed] + replaced_char + s[idx_to_placed + 1:]
        except StopIteration:
            return s
