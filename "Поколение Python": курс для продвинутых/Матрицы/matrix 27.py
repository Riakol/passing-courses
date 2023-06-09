n, m = [int(i) for i in input().split()]
matrix_a = [[int(i) for i in input().split()] for _ in range(n)]
empty_row = input()
matrix_b = [[int(i) for i in input().split()] for _ in range(n)]
matrix_c = []

for i in range(n):
    row = []
    for j in range(m):
        row.append(matrix_a[i][j] + matrix_b[i][j])
    matrix_c.append(row)

for i in range(n):
    for j in range(m):
        print(str(matrix_c[i][j]).ljust(3), end=' ')
    print()
    