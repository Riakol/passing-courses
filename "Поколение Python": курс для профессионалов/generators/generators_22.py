def around(iterable):
    wrapper = [None] + list(iterable) + [None]
    for i in range(len(wrapper) - 2):
        yield (wrapper[i], wrapper[i + 1], wrapper[i + 2])