def get_min_max(iterable):
    try:
        iterator = iter(iterable)
        first_item = next(iterator)
    except StopIteration:
        return None
    
    min_item = max_item = first_item
    
    for item in iterator:
        if item < min_item:
            min_item = item
        if item > max_item:
            max_item = item
    
    return min_item, max_item

