num = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(num)]
second_matrix = [[0] * num for _ in range(num)] 

for i in range(num):
    for j in range(num):
        second_matrix[j][i] = matrix[i][j]

for i in range(num):
    for j in range(num):
        print(str(second_matrix[i][j]).ljust(2), end=' ')
    print()
    