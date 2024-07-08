from functools import wraps

def takes(*f_funcs_args):
    def dec(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if all(type(i) in f_funcs_args for i in (*args, *kwargs.values())): 
                return result 
            else: raise TypeError
        return wrapper
    return dec
