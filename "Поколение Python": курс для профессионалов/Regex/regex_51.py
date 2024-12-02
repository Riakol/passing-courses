import re

def multiple_split(string, delimeters):
    pattern = '|'.join(re.escape(x) for x in delimeters)
    return re.split(rf'{pattern}', string)
