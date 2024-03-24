import time

def get_the_fastest_func(funcs, arg):
    result = {}
    for func in funcs:
        start = time.perf_counter()
        func(arg)
        end = time.perf_counter()
        result[end-start] = func
    return result[min(result)]
