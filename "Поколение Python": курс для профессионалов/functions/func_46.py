from functools import wraps

class MaxRetriesException(Exception):
    pass

def retry(times):
    def deca(functs):
        @wraps(functs)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                try: 
                    result = functs(*args, **kwargs)
                    return result
                except Exception as e:
                    error = e
            raise MaxRetriesException from error
        return wrapper
    return deca

