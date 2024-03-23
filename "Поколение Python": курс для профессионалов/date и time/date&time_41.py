import time

def calculate_it(func, *args):
    start = time.perf_counter()
    res = func(*args)
    end = time.perf_counter()
    return (res, end-start)