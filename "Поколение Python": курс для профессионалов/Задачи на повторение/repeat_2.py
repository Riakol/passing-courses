def same_parity(numbers):
    return list(filter(lambda x: x % 2 == 0 if numbers[0] % 2 == 0 else x % 2 != 0, [i for i in numbers]))

