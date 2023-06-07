n, m = int(input()), int(input())
matrix = []

for i in range(n):
    matrix.append(input().split())

largest, indexes = int(matrix[0][0]), '0 0'

for i in range(n):
    for j in range(m):
        if int(matrix[i][j]) > largest:
            largest = int(matrix[i][j])
            indexes = f'{i} {j}'
print(indexes)
