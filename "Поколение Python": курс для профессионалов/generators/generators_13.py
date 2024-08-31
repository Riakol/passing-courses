def interleave(*args):
    for x in zip(*args):
        yield from x