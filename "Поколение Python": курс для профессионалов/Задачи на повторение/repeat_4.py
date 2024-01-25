def print_given(*args, **kwargs):
    for i in args:
        print(i, type(i))
    for k in sorted(kwargs.keys()):
        print(k, kwargs[k], type(kwargs[k]))
