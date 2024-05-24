def get_pow(x, n):
    if n == 0:
        return 1
    else:
        return x * get_pow(x, n - 1)
