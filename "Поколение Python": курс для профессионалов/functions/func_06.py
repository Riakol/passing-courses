def custom_isinstance(objects, typeinfo):
    return sum([1 if isinstance(i, typeinfo) == True else 0 for i in objects])

