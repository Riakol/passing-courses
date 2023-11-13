# put your python code here
def summator(x):
    return sum([int(i) for i in str(x)])

# n = sorted(input().split(), reverse=False)
n = sorted([int(i) for i in input().split()])

print(*sorted(n, key=summator))
