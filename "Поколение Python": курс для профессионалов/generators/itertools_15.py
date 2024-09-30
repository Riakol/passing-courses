import itertools as it

def grouper(iterable, n):
    return it.zip_longest(*[iter(iterable)] * n)