def is_iterable(obj):
    try:
        iter1 = iter(obj)
        for _ in iter1:
            next(iter(obj))
        return True
    except TypeError:
        return False

    