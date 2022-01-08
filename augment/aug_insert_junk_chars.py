import random

from resources import list_junk_charaters
from .base_operation import BaseOperation


class InsertJunkCharacters(BaseOperation):
    """Insert meaningless a character into text"""

    def __init__(self):
        super(InsertJunkCharacters, self).__init__()
        self.junk_chars = list_junk_charaters()

    def __call__(self, s):
        idx = random.randint(0, len(s))
        char_to_insert = random.choice(self.junk_chars)
        return s[:idx] + char_to_insert + s[idx:]
