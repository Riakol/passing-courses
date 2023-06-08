n, m = [int(i) for i in input().split()]
matrix = [[1] * m for _ in range(n)]
total = 0

for k in range(n * m):
    for i in range(n):
        for j in range(m):
            if i + j == k:
                total += 1
                matrix[i][j] = total

for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end=' ')
    print()
    