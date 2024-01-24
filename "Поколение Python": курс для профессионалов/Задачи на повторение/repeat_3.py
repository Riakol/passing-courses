def is_valid(string):
    if len(string.split()) > 1:
        return any([i for i in string.split() if 0 <= int(i) <= 9 and i.isdigit()]) and 4 <= len(string.replace(' ', '')) <= 6
    else:
        return string.replace(' ', '').isdigit() and 4 <= len(string.replace(' ', '')) <= 6
    