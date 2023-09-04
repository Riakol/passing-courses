# put your python code here
encrypted = input()
n = int(input())
dct = {}

for _ in range(n):
    letter, number = input().split(":")
    dct[number.strip()] = letter

for i in encrypted:
    print(dct[str(encrypted.count(i))], end='')