def parse_ranges(ranges):
    for i in ranges.split(','):
        a, b = i.split('-')
        yield from range(int(a), int(b) + 1)