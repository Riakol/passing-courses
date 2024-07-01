import functools

def returns_string(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if type(result) == str:
                return result
            else:
                raise TypeError
    return wrapper
