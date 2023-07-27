# put your python code here
num, num2, num3 = set(int(i) for i in input().split()), set(int(i) for i in input().split()), set(int(i) for i in input().split())

print(*sorted(num3 - (num | num2), reverse=True))




