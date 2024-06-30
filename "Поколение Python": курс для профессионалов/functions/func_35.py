import functools

def square(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs) ** 2
        return result
    return wrapper
