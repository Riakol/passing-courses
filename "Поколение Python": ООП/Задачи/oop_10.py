import re

def is_fraction(string):
    return bool(re.fullmatch( r'-?\d+/0*[1-9]+\d*', string))