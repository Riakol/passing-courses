def polynom(x):
    if not hasattr(polynom, 'values'):
        polynom.values = set()
    polynom.values.add(x**2 + 1)
    return x**2 + 1
