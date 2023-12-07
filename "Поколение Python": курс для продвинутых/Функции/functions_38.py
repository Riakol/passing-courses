# put your python code here
a, b = [int(input()) for _ in range(2)]

print(*list(map(lambda x: x, [int(i) for i in list(map(lambda x: [False, x][all(x % int(i) == 0 for i in str(x))], [i for i in list(filter(lambda x: '0' not in str(x), range(a, b + 1)))])) if i != False])))




