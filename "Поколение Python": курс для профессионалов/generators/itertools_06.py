import itertools

def drop_this(iterable, obj):
    yield from (itertools.dropwhile(lambda num: num == obj, iterable))
