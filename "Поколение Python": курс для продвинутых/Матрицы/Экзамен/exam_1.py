symbols = input().split()
num = int(input())
temp = []


for i in symbols[:num]:
    row = []
    for j in range(symbols.index(i), len(symbols), num):
        row.append(symbols[j])
    temp.append(row)

print(temp)
