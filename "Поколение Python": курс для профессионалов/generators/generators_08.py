def flatten(nested_list):
    for i in nested_list:
        if type(i) is list:
            yield from flatten(i)
        else:
            yield i

