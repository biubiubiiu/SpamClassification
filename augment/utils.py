import random


def zip_with_next(x):
    return zip(x, x[1:])


def random_replace(this, other, num_replace):
    idxs_to_replaced = random.sample(range(len(this)), num_replace)
    if max(idxs_to_replaced) < min(len(this), len(other)):  # TODO remove this sanity check
        for idx in idxs_to_replaced:
            this[idx] = other[idx]
    return this
