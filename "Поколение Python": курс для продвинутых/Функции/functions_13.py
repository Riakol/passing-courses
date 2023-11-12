# put your python code here
def summator(x):
    total = 0
    for i in x:
        total += int(i)
    return total

n = input().split()

print(*sorted(n, key=summator))
