from itertools import count

def tabulate(func):
    counter = count(1)
    for num in counter:
        yield func(num)