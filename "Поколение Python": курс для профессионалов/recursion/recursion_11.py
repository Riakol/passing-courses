def number_of_frogs(x):
    if x == 1:
        return 77
    else:
        return (3 * (number_of_frogs(x - 1) - 30))
