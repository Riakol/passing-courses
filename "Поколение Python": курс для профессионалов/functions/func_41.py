from functools import wraps

def strip_range(start, end, char='.'):
    def dec(func):
        @wraps(func)
        def symbol_changer(*args, **kwargs):
            nonlocal end
            copy_var = list(func(*args, **kwargs))
            end = len(copy_var) if end > len(copy_var) - 1 else end
            for i in range(start, end):
                copy_var[i] = char
            return ''.join(copy_var)
        return symbol_changer
    return dec
