# put your python code here
num, num2, num3 = set(input().split()), set(input().split()), set(input().split())

alltogether = num | num2 | num3
peresechenie = num & num2 & num3

print(*sorted(alltogether - peresechenie, reverse=False, key=int))