import itertools

def first_true(iterable, predicate=None):
    try:
        return next(itertools.filterfalse(lambda x: not x > 0 if predicate is None else not predicate(x), iterable))
    except StopIteration:
        return None
    