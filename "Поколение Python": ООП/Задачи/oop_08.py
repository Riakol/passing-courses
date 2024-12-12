import re

def is_integer(string):
    return bool(re.fullmatch(r'-\d+|\d+', string))