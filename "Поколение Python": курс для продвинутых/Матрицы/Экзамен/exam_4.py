num = int(input())
matrix = [['.' for _ in range(num)] for _ in range(num)]

for i in range(num):
    for j in range(num):
        if i == j or i == num - j - 1:
            matrix[i][j], matrix[i][num // 2], matrix[num // 2][j] = '*', '*', '*'
            

for i in range(num):
    for j in range(num):
        print(str(matrix[i][j]).ljust(2), end=' ')
    print()
    