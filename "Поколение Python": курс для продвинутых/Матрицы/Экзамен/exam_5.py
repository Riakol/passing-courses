num = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(num)]

for i in range(num):
    for j in range(num):
        if matrix[i][j] != matrix[num - j - 1][num - i - 1]:
            exit(print('NO'))
        else:
            exit(print('YES'))
            