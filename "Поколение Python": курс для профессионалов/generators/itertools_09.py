import itertools as it

def take_nth(iterable, n):
    return next(it.islice(iterable, n-1, n), None)