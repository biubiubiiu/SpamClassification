import random


def is_chinese_character(c):
    if isinstance(c, str):
        assert len(c) == 1
        c = c[0]
    return '\u4e00' <= c <= '\u9fa5'


def zip_with_next(x):
    return zip(x, x[1:])


def random_replace(this, other, num_replace):
    idxs_to_replaced = random.sample(range(len(this)), num_replace)
    if max(idxs_to_replaced) < min(len(this), len(other)):  # TODO remove this sanity check
        for idx in idxs_to_replaced:
            this[idx] = other[idx]
    return this


def first(iterable, predicate=lambda x: True):
    """
    Returns the first item in the `iterable` that
    satisfies the `condition`.

    If the condition is not given, returns the first item of
    the iterable.

    Raises `StopIteration` if no item satisfying the condition is found.
    """

    return next(x for x in iterable if predicate(x))
