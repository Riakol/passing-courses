def alternating_sequence(count=None):
    x = 0
    while x != count:
        x += 1
        yield [-1, 1][x % 2] * x

