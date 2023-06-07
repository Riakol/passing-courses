row, col = int(input()), int(input())
result = []

for i in range(row):
    r = []
    for j in range(col):
        r.append(input())
    result.append(r)

for r in range(row):
    for c in range(col):
        print(result[r][c], end=' ')
    print()
print()

for c in range(col):
    for r in range(row):
        print(result[r][c], end=' ')
    print()