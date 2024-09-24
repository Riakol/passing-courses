def first_largest(iterable, n):
    wrapper = list(iterable)
    for num in range(len(wrapper)):
        if wrapper[num] > n:
            return num
        else:
            continue
    else:
        return -1