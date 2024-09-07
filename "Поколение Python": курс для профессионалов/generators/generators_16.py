def filter_names(names, ignore_char, max_names):
    mylist = [elem for elem in names if not ignore_char.lower() in elem[0].lower() and not any(char.isdigit() for char in elem)]
    yield from mylist[:max_names]