n = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]
table = [i for i in range(1, n * n + 1)]
summary = int((n**2 * (n**2 + 1) / 2) / n)

for i in matrix:
    for j in i:
        if j in table:
            table.pop(table.index(j))

if not table:
    for i in range(n):
        temp_vert = 0
        temp_horz = 0
        for j in range(n):
            temp_vert += matrix[j][i]
            temp_horz += matrix[i][j]
        if temp_vert == summary and temp_horz == summary and sum(matrix[i][i] for i in range(n)) == summary and sum(matrix[i][n - i - 1] for i in range(n)) == summary:
            continue
        else:
            exit(print('NO'))
    exit(print('YES'))
else:
    print('NO')
    