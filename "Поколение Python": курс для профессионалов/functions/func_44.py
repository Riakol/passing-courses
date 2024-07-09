from functools import wraps

def add_attrs(**f_funcs_kwargs):
    def dec(func):
        for k, v in f_funcs_kwargs.items():
            func.__dict__[k] = v 
        func.__dict__['k'] = f_funcs_kwargs
        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper
    return dec
