import itertools

def drop_while_negative(iterable):
    func = list(itertools.dropwhile(lambda num: num < 0, iterable))
    yield from func