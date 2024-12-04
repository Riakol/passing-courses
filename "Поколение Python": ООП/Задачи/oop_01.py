# put your python code here
num = int(input())
matrix = [[1] * num for _ in range(num)]

for i in range(num):
    for j in range(num):
        matrix[i][j] = min(i + 1, j + 1, num - i, num - j)

for row in matrix:
    print(*row)

