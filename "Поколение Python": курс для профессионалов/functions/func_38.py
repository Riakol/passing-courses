import functools

def prefix(string, to_the_end=False):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            return f"{res}{string}" if to_the_end else f"{string}{res}"
        return wrapper
    return decorator
