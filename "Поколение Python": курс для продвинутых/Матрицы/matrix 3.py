num = int(input())
arr = [input().split() for i in range(num)]
total = 0

for i in range(num):
    total += int(arr[i][i])
print(int(total))