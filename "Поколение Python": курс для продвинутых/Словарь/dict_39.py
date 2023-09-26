def merge(values):
    temp = {}
    for value in values:
        for key, val in value.items():
            temp.setdefault(key, set()).add(val)
    return temp