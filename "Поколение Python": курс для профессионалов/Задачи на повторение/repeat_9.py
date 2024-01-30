def spell(*args):
    return {i[0].lower(): len(max(args, key=lambda x: len(x) if str(x).lower().startswith(i[0].lower()) else 0)) for i in args}
