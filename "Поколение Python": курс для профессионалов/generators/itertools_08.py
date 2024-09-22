import itertools as it

def take(iterable, n):
    yield from it.islice(iterable, n)