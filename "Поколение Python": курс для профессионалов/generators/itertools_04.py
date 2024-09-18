from itertools import zip_longest

def roundrobin(*args):
    for x in zip_longest(*args, fillvalue=' '):
        for n in x:
            if n == ' ':
                continue
            else:
                yield n