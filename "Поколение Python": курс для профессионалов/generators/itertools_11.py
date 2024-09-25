def sum_of_digits(iterable):
    return sum(list(map(int, ''.join(list(map(str, iterable))))))