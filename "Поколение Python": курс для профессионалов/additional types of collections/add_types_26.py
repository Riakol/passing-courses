from collections import ChainMap

def deep_update(chainmap, key, value):
    if key in chainmap:
        for i in chainmap.maps:
            if key in i:
                chainmap.maps[chainmap.maps.index(i)][key] = value
    else:
        chainmap[key] = value
        