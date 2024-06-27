def do_twice(func):
    def making_two(*args, **kwargs):
        res = func(*args, **kwargs)
        res = func(*args, **kwargs)
        return res
    return making_two

