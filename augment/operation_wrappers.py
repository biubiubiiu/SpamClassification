import random

from .base_operation import BaseOperation
from .base_wrapper import BaseWrapper
from .utils import first


class Repeat(BaseWrapper):
    """Wrapper class for repeating operation

    Args:
        ops (BaseOperation): operation
        repeat_times (int): times to repeat
    """

    def __init__(self, ops, repeat_times):
        super(Repeat, self).__init__(ops)

        if not isinstance(repeat_times, int) or repeat_times <= 0:
            raise ValueError('repeat times should greater than 1 integer')

        self.repeat_times = repeat_times

    def transform(self, s):
        ret = s
        for _ in range(self.repeat_times):
            ret = self.ops.transform(ret)
        return ret


class CharReplacement(BaseWrapper):
    """A general wrapper for char level replacement

    Args:
        random_pick (bool): if `True`, random pick one character to replace, else
                find the first character the can be replaced. Default: `True`

    Returns:
        The transformed text with one character replaced, or the original text if
        transformation coule be done
    """

    def __init__(self, ops, random_pick=True):
        super(CharReplacement, self).__init__(ops)
        self.random_pick = random_pick

    def transform(self, s):
        try:
            # filter characters that cant be replaced
            idxs = list(filter(lambda idx: self.can_replace(s[idx]), range(len(s))))
            if self.random_pick:
                random.shuffle(idxs)
            idx_to_replace = first(idxs)
            char_to_replace = s[idx_to_replace]
            replaced_char = self.ops.transform(char_to_replace)
            return s[:idx_to_replace] + replaced_char + s[idx_to_replace + 1:]
        except StopIteration:
            return s
