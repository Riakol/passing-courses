# put your python code here
num, num2, num3 = set(int(i) for i in input().split()), set(int(i) for i in input().split()), set(int(i) for i in input().split())

score = {int(i) for i in range(11)}

print(*sorted(score - (num | num2 | num3)))