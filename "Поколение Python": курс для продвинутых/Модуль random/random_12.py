from random import sample
from string import *

LETTER = ''.join((set(ascii_letters) | set(digits)) - set('lI1oO0'))

def generate_password(length):
    return ''.join(sample(LETTER, length))

def generate_passwords(count, length):
    for _ in range(count):
        print(generate_password(length))

generate_passwords(int(input()), int(input()))