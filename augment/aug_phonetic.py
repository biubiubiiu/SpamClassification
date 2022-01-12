import random

from resources import dict_char_to_phonetic

from .base_operation import BaseOperation
from .utils import is_chinese_character


class ToPhonetic(BaseOperation):
    """Replace characters to its phonetically similar ones"""

    def __init__(self):
        super(ToPhonetic, self).__init__()
        self.dict = dict_char_to_phonetic()

    def can_replace(self, s):
        return any(is_chinese_character(c) and c in self.dict for c in s)

    def transform(self, s):
        chars = list(s)
        for i, c in enumerate(chars):
            chars[i] = random.choice(self.dict.get(c, c))
        return ''.join(chars)
