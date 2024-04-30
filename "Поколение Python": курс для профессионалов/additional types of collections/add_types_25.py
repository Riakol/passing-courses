from collections import ChainMap

def get_all_values(chainmap, key):
    close = set()
    for i in chainmap.maps:
        if key in i:
            close.add(i[key])
    return close if close else set()
