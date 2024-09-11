def with_previous(iterable):
    temp = [None]
    for i in iterable:
        yield (i, temp[-1])
        temp.append(i)