from math import factorial

def factorials(n):
    for i in range(1, n + 1):
        yield factorial(i)