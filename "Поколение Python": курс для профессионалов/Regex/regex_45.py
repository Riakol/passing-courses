import re

def normalize_whitespace(string):
    return re.sub(r' {2,}', r' ', string)

