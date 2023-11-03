def greet(name, *args):
    if args:
        return f"Hello, {name} and {' and '.join(args)}!"
    else:
        return f"Hello, {name}!"