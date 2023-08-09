# put your python code here
n, m = [input().split() for _ in range(2)]

if set(n) == set(m):
    print('YES')
else:
    print('NO')