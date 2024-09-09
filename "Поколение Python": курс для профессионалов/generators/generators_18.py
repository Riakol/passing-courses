def unique(iterable):
    wrapper = list(iterable)
    row = []
    for n in wrapper:
        if n not in row:
            row.append(n)
    yield from row