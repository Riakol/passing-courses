def get_biggest(numbers):
    if numbers:
        res = sorted(numbers, reverse=True, key=lambda x: str(x) * max(numbers))
        return int(''.join(map(str, res)))
    else:
        return -1
