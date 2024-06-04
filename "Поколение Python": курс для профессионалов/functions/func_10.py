def zip_longest(*args, fill=None):
    lengths = [len(i) for i in args]
    if min(lengths) == max(lengths):
        return [i for i in zip(*args)]
    else:
        for i in args:
            if len(i) < max(lengths):
                for _ in range(max(lengths)-len(i)):
                    args[args.index(i)].append(fill)
        for i in args:
            return [c for c in zip(*args)]
