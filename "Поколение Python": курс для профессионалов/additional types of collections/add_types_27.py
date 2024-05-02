from collections import ChainMap

def get_value(chainmap, key, from_left=True):
    if key in chainmap:
        if from_left:
            for i in chainmap.maps:
                if key in i:
                    return i[key]
        else:
            for i in chainmap.maps[::-1]:
                return i[key]
    else:
        return None
