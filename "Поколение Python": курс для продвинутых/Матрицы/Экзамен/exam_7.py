col,row = list(input())
x = 'abcdefgh'.find(col)
y = abs(8 - int(row))

chess = []

for i in range(8):
    chess.append(list('.' * 8))

for i in range(8):
    for j in range(8):
        if j == y or i == x or i == x + y - j or j == y - x + i :
            chess[j][i] = '*'

chess[y][x] = 'Q'
for i in chess:
    print(*i)
    