def print_operation_table(operation, rows, cols):
    matrix = []
    for i in range(1, rows + 1):
        row = []
        for j in range(1, cols + 1):
            row.append(operation(i , j))
        matrix.append(row)
    for iter in matrix:
        print(*iter)
