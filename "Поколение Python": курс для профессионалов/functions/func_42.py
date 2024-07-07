from functools import wraps

def returns(datatype):
    def dec(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if type(result) == datatype: 
                return result 
            else:
                raise TypeError
        return wrapper
    return dec
