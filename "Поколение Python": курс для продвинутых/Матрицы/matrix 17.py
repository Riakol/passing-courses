row, col = [int(i) for i in input().split()]
matrix = []

for i in range(row):
    temp = []
    for j in range(col):
        if i % 2 == j % 2:
            temp.append('.')
        else:
            temp.append('*')
    matrix.append(temp)

for i in matrix:
    print(*i)
    