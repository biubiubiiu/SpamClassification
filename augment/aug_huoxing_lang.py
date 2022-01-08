import random

from resources import dict_char_to_huoxing_lang
from .base_operation import BaseOperation
from .utils import first


class CharacterToHuoxing(BaseOperation):
    """Replace single character to HuoXing Language

    Args:
        random_pick (bool): if `True`, random pick one character to replace, else
                find the first character the can be replaced. Default: `True`

    Returns:
        The transformed text with one character replaced, or the original text if no
        transformation coule be done
    """

    def __init__(self, random_pick=True):
        super(CharacterToHuoxing, self).__init__()
        self.dict = dict_char_to_huoxing_lang()
        self.random_pick = random_pick

    def __call__(self, s):
        assert isinstance(s, str), f'Input should be a string, but got {type(s)}'

        try:
            idxs = list(range(len(s)))
            if self.random_pick:
                random.shuffle(idxs)
            idx_to_replace = first(idxs, lambda idx: s[idx] in self.dict)
            replaced_char = self.dict[s[idx_to_replace]]
            return s[:idx_to_replace] + replaced_char + s[idx_to_replace + 1:]
        except StopIteration:
            return s


class SentenceToHuoxing(BaseOperation):
    """Replace all characters to Huoxing Language

    Returns:
        The transformed text.
    """

    def __int__(self):
        super(SentenceToHuoxing, self).__init__()
        self.dict = dict_char_to_huoxing_lang()

    def __call__(self, s):
        assert isinstance(s, str), f'Input should be a string, but got {type(s)}'
        chars = list(s)
        for i, c in enumerate(chars):
            chars[i] = self.dict.get(c, default=c)
        return ''.join(chars)
