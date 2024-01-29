def index_of_nearest(numbers, number):
    if numbers:
        return numbers.index(min(numbers, key=lambda x: abs(x - number)))
    else:
        return -1
