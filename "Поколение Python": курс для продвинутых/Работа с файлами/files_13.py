from random import choice

with open('first_names.txt', 'r', encoding='utf-8') as first, open('last_names.txt', 'r', encoding='utf-8') as last:
    first_n, last_n = first.readlines(), last.readlines()
    for i in range(3):
        print(choice(first_n).strip(), choice(last_n).strip())
