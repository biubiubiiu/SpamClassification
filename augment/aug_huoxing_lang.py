from resources import dict_char_to_huoxing_lang
from .base_operation import BaseOperation


class ToHuoxing(BaseOperation):
    """Replace characters to HuoXing Language

    Args:
        random_pick (bool): if `True`, random pick one character to replace, else
                find the first character the can be replaced. Default: `True`

    Returns:
        The transformed text with one character replaced, or the original text if no
        transformation coule be done
    """

    def __init__(self):
        super(ToHuoxing, self).__init__()
        self.dict = dict_char_to_huoxing_lang()

    def can_replace(self, s):
        return any(c in self.dict for c in s)

    def transform(self, s):
        chars = list(s)
        for i, c in enumerate(chars):
            chars[i] = self.dict.get(c, c)
        return ''.join(chars)
