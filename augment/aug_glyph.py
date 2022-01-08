from resources import dict_char_to_shape_closed
from .base_operation import BaseOperation
from .utils import is_chinese_character


class ToGlyphSimilar(BaseOperation):
    """Replace chinese characters to its glyph-similar one"""

    def __init__(self):
        super(ToGlyphSimilar, self).__init__()
        self.dict = dict_char_to_shape_closed()

    def can_replace(self, s):
        return any(is_chinese_character(c) for c in s)

    def transform(self, s):
        chars = list(s)
        for i, c in enumerate(chars):
            chars[i] = self.dict.get(c, c)
        return ''.join(chars)
