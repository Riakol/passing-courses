import itertools as it

def max_pair(iterable):
    return max(sum(x) for x in it.pairwise(iterable))