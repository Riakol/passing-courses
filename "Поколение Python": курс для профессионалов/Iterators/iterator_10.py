def is_iterator(obj):
    return '__iter__' in dir(obj) and '__next__' in dir(obj)


