num = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(num)]
checker = [i for i in range(1, num + 1)]

for i in range(num):
    nums = []
    nums_2 = []
    for j in range(num):
        if matrix[i][j] not in nums and matrix[i][j] in checker:
            nums.append(matrix[i][j])
        else:
            exit(print('NO'))
        if matrix[j][i] not in nums_2 and matrix[j][i] in checker:
            nums_2.append(matrix[j][i])
        else:
            exit(print('NO'))
else:
    print('YES')
    