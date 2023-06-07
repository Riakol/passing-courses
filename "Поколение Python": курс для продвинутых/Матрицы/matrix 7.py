size_matrix = int(input())
matrix = []
r, l, u, b = 0, 0, 0, 0

for _ in range(size_matrix):
    temp = [int(i) for i in input().split()]
    matrix.append(temp)

for i in range(size_matrix):
    for j in range(size_matrix):
        if i < j and i < size_matrix - 1 - j:
           u += matrix[i][j]
        if i < j and i > size_matrix - 1 - j:
           r += matrix[i][j]
        if i > j and i > size_matrix - 1 - j:
           b += matrix[i][j]
        if i > j and i < size_matrix - 1 - j:
           l += matrix[i][j]

print(f"Верхняя четверть: {u}\nПравая четверть: {r}\nНижняя четверть: {b}\nЛевая четверть: {l}")
