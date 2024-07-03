import functools

def make_html(tag):
    def decor(func):
        @functools.wraps(func)
        def inner_func(*args, **kwargs):
            answer = func(*args, **kwargs)
            return f"<{tag}>{answer}</{tag}>"
        return inner_func
    return decor
