def stop_on(iterable, obj):
    for n in iterable:
        if n == obj:
            break
        yield n
