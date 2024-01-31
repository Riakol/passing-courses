def choose_plural(amount, declensions):

    first, second, third = declensions
    if amount % 10 == 1 and amount % 100 != 11:
        return f"{amount} {first}"
    elif 2 <= amount % 10 <= 4 and (amount % 100 < 10 or amount % 100 >= 20):
        return f"{amount} {second}"
    else:
        return f"{amount} {third}"
