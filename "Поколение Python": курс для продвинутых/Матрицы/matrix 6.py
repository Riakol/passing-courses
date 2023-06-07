square_num = int(input())
matrix = []

for _ in range(square_num):
    temp = [int(i) for i in input().split()]
    matrix.append(temp)

largest = matrix[0][0]

for i in range(square_num):
    for j in range(square_num):
        if i >= j and i <= square_num - 1 - j and matrix[i][j] > largest:
            largest = matrix[i][j]
        elif i <= j and i >= square_num - 1 - j and matrix[i][j] > largest:
            largest = matrix[i][j]

print(largest)
