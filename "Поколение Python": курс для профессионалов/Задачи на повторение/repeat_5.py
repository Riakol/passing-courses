def convert(string):
    is_up = len([i for i in string if i.isalpha() and i.isupper()])
    is_low = len([i for i in string if i.isalpha() and i.islower()])
    if is_low >= is_up:
        return string.lower()
    else:
        return string.upper()
