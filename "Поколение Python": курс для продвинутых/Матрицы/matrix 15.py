col,row = list(input())
x = 'abcdefgh'.find(col)
y = abs(8 - int(row))

chess = []

for i in range(8):
    chess.append(list('.' * 8))

for i in range(8):
    for j in range(8):
        inx = (y-j) * (x - i)
        if inx == 2 or inx == -2:
            chess[j][i] = '*'

chess[y][x] = 'N'
for i in chess:
    print(*i)
    