import itertools as it

def is_rising(iterable):
    return all(x < y for x, y in it.pairwise(iterable))