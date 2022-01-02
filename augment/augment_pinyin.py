import math
from typing import Set

from pypinyin import lazy_pinyin

from .utils import random_replace


def pinyin_augment(line: str) -> Set[str]:
    pinyin = lazy_pinyin(line)
    chars = list(line)
    augmented = set()

    # 随机选两个字换成拼音
    for _ in range(math.floor(math.sqrt(len(pinyin)))):
        sample = random_replace(chars, pinyin, 2)
        augmented.add(''.join(sample))

    # TODO jiema 分词，整个词换成拼音
    return augmented
