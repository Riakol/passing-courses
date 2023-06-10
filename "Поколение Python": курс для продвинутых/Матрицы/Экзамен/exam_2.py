num = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(num)]
largest = matrix[0][0]

for i in range(num):
    for j in range(num):
        if i >= j and i > num - 1 - j or i <= j and i > num - 1 - j or i == num - j - 1:
            if matrix[i][j] > largest:
                largest = matrix[i][j]
print(largest)
