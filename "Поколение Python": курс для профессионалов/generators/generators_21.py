def pairwise(iterable):
    iterable = list(iterable)
    for i in range(len(iterable)):
        if i + 1 == len(iterable):
            yield (iterable[i], None)
        else:
            yield (iterable[i], iterable[i + 1])

