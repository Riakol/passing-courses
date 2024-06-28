def reverse_args(func):
    def wrapper(*args, **kwargs):
        m = func(*args[::-1], **kwargs)
        return m
    return wrapper

