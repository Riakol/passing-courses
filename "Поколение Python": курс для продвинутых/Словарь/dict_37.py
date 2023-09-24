# put your python code here
letter = input().upper()
summa = 0
Scrabble = {1: ['A', 'E', 'I', 'L', 'N', 'O', 'R', 'S', 'T', 'U'],
            2: ['D', 'G'],
            3: ['B', 'C', 'M', 'P'],
            4: ['F', 'H', 'V', 'W', 'Y'],
            5: 'K',
            8: ['J', 'X'],
            10: ['Q', 'Z']}

for i in letter:
    for key, values in Scrabble.items():
        if i in values:
            summa += key

print(summa)