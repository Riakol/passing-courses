# put your python code here
n = int(input())
cities = {input() for _ in range(n + 1)}

if len(cities) == n + 1:
    print('OK')
else:
    print('REPEAT')