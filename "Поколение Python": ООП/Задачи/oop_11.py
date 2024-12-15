def intersperse(iterable, delimiter):
    if iterable:
        it = iter(iterable)
        yield next(it)
        for item in it:
            yield delimiter
            yield item
            
            