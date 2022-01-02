import math
from typing import Set

from hanziconv import HanziConv

from .utils import random_replace


def simplified2traditional_augment(line: str) -> Set[str]:
    chars = list(line)
    traditional = HanziConv.toTraditional(line)
    augmented = set()

    # 随机选两个字换成繁体
    for _ in range(math.floor(math.sqrt(len(traditional)))):
        sample = random_replace(chars, traditional, 2)
        augmented.add(''.join(sample))

    # TODO jiema 分词，整个词换
    return augmented
