def add3(x):
    return x + 3


def mul7(x):
    return x * 7

def func_apply(function, items):
    result = []
    for i in items:
        result.append(function(i))
    return result
