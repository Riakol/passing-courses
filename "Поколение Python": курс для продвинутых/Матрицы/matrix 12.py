n = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == j:
            matrix[i][j], matrix[n-i-1][i] = matrix[n-i-1][i], matrix[i][j]

for k in matrix:
    print(*k)
    