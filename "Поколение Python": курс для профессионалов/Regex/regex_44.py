import re

def normalize_jpeg(filename):
    return re.sub(r'(jpeg|jpg)$', r'jpg', filename, flags=re.IGNORECASE)

