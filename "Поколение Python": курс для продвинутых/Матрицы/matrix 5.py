sqr = int(input())
arr = [list(map(int, input().split())) for _ in range(sqr)]
largest = arr[0][0]
indx = 0

for i in arr:
    indx += 1
    for j in range(indx - indx, indx):
        if i[j] >= largest:
            largest = i[j]
        if indx == sqr * (sqr + 1) / 2:
            break       
print(largest)