def fill_spiral_matrix(n, m):
    matrix = [[0] * m for _ in range(n)]
    num = 1
    row_start = 0
    row_end = n - 1
    col_start = 0
    col_end = m - 1

    while row_start <= row_end and col_start <= col_end:
        # Заполнение верхней строки
        for j in range(col_start, col_end + 1):
            matrix[row_start][j] = num
            num += 1
        row_start += 1

        # Заполнение правого столбца
        for i in range(row_start, row_end + 1):
            matrix[i][col_end] = num
            num += 1
        col_end -= 1

        # Заполнение нижней строки
        if row_start <= row_end:
            for j in range(col_end, col_start - 1, -1):
                matrix[row_end][j] = num
                num += 1
            row_end -= 1

        # Заполнение левого столбца
        if col_start <= col_end:
            for i in range(row_end, row_start - 1, -1):
                matrix[i][col_start] = num
                num += 1
            col_start += 1

    return matrix

n, m = [int(i) for i in input().split()]
spiral_matrix = fill_spiral_matrix(n, m)
for row in spiral_matrix:
    print(' '.join(str(cell).ljust(3) for cell in row))