import re

def is_decimal(string):
    return bool(re.fullmatch(r'-\.\d+|-\d+\.?\d+|\d+\.|\d+\.?\d+|\.\d+|-\d+\.?', string))

