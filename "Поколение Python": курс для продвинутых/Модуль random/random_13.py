from random import sample
from string import *

LETTER = ''.join((set(ascii_letters) | set(digits)) - set('lI1oO0'))

def generate_password(length):
    password = []
    password += sample(''.join((set(digits)) - set('lI1oO0')), 1)
    password += sample(''.join((set(ascii_uppercase)) - set('lI1oO0')), 1)
    password += sample(''.join((set(ascii_lowercase)) - set('lI1oO0')), 1)
    return f"{''.join(sample(LETTER, length - 3))}{''.join(password)}"


def generate_passwords(count, length):
    for _ in range(count):
        print(generate_password(length))

generate_passwords(int(input()), int(input()))