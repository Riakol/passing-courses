n, m = int(input()), int(input())
mtrx = [[int(i) for i in input().split()] for _ in range(n)]
exchange = [[int(i) for i in input().split()] for _ in range(1)]

for i in mtrx:
    i[exchange[0][0]], i[exchange[0][1]] = i[exchange[0][1]], i[exchange[0][0]]
    print(*i)
