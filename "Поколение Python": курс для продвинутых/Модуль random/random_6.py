from random import randint as ri

def generate_index():
    return f"{chr(ri(65, 90))}{chr(ri(65, 90))}{ri(0, 99)}_{ri(0, 99)}{chr(ri(65, 90))}{chr(ri(65, 90))}"
