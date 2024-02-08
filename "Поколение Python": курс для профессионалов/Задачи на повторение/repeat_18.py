input_data = {s: m for s, m in (input().split('@') for _ in range(int(input())))}
x = 1

for i in range(int(input())):
    surname = input()
    if surname not in input_data.keys():
        input_data[surname] = surname + '@beegeek.bzz'
        print(f"{surname}@beegeek.bzz")
    else:
        key = surname
        while key in input_data.keys():
            idx = sum(c.isdigit() for c in key)
            if idx >= 1: 
                key = surname + str(int(key[-idx:]) + x)
            else:
                key = surname + str(x)
        input_data[key] = '@beegeek.bzz'
        print(f"{key}@beegeek.bzz")
        