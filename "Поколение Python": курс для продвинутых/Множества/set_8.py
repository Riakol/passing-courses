text = input()

if len(text) == len(set(text)):
    print('YES')
else:
    print('NO')