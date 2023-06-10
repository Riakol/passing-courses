num = int(input())
matrix = [[0] * num for _ in range(num)]

for i in range(num):
    for j in range(num):
        matrix[i][j] = abs(i - j)

for i in range(num):
    for j in range(num):
        print(str(matrix[i][j]).ljust(2), end=' ')
    print()
    