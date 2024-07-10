from functools import wraps

def ignore_exception(*f_first_args): 
    def dec(func): 
        @wraps(func) 
        def wrapper(*args, **kwargs): 
            try:   
                return func(*args, **kwargs)
            except f_first_args as e:
                print(f"Исключение {e.__class__.__name__} обработано") 
        return wrapper 
    return dec
