def cubes_of_odds(iterable):
    yield from (number ** 3 for number in iterable if number % 2)

