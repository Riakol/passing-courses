def simple_sequence():
    x = 0
    while True:
        x += 1
        for _ in range(1, x + 1):
            yield x

            