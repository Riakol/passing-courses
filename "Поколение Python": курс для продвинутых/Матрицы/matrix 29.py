n, m = [int(i) for i in input().split()]
matrix_a = [[int(i) for i in input().split()] for _ in range(n)]
empty_row = input()
l, k = [int(i) for i in input().split()]
matrix_b = [[int(i) for i in input().split()] for _ in range(l)]
matrix_c = []
g = k

if n > l:
    for i in range(n):
        fix = []
        for j in range(n):
            temp = 0
            row = []
            for k in range(l):
                if g == 1:
                    row.append(matrix_a[i][k] * matrix_b[k][k])
                else:
                    row.append(matrix_a[i][k] * matrix_b[k][j])
            temp += sum(row)
            fix.append(temp)
        matrix_c.append(fix)
    
    for i in range(n):
        for j in range(n):
            print(matrix_c[i][j], end=' ')
        print()

else:
    for i in range(n):
        temp = []
        for j in range(m):
            row = []
            for k in range(n):
                if g == 1:
                    row.append(matrix_a[i][k] * matrix_b[k][k])
                else:
                    row.append(matrix_a[i][k] * matrix_b[k][j])
            temp.append(sum(row))
        matrix_c.append(temp)

    for i in range(n):
        if matrix_c[i][j] == 0:
            for j in range(m - 1):
                print(matrix_c[i][j], end=' ')
            print()
        else:
            for j in range(m):
                print(matrix_c[i][j], end=' ')
            print()
            