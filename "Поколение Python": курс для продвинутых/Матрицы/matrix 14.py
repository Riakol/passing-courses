num = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(num)]
indx = -1

for i in range(num, 0, -1):
    indx += 1
    for j in matrix[::-1]:
        for k in range(1):
            print(j[indx], end=' ')
    print()
    