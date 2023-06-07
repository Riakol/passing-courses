num = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(num)]

for i in matrix[::-1]:
    print(*i)
    