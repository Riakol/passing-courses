def sort_priority(values, group):
    values[:] = sorted(sorted(values), key=lambda x: x in group, reverse=True)
    return values

