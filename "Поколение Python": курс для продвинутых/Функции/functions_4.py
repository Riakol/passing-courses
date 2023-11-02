def mean(*args):
    x, y = 0, 0
    for i in args:
        if type(i) in (int, float):
            x += i
            y += 1
    if y > 0:
        return x/y
    else:
        return float(y)