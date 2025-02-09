class Matrix:
    def __init__(self, rows, cols, value=0) -> None:
        self.rows = rows
        self.cols = cols
        self.value = value
        self._matrix = [[value] * cols for _ in range(rows)]
    
    def get_value(self, row, col):
        return self._matrix[row][col]

    def set_value(self, row, col, value):
        self._matrix[row][col] = value

    def __repr__(self) -> str:
        return f'Matrix({self.rows}, {self.cols})'
    
    def __str__(self) -> str:
        str_matrix = [[str(elem) for elem in row] for row in self._matrix]
        return '\n'.join(' '.join(row) for row in str_matrix)

    def __pos__(self):
        mtrx = Matrix(self.rows, self.cols)
        for row in range(mtrx.rows):
            for col in range(mtrx.cols):
                mtrx.set_value(row, col, self.get_value(row, col))
        return mtrx
    
    def __neg__(self):
        mtrx = Matrix(self.rows, self.cols)
        for row in range(mtrx.rows):
            for col in range(mtrx.cols):
                mtrx.set_value(row, col, -self.get_value(row, col))
        return mtrx

    def __invert__(self):
        mtrx = Matrix(self.cols, self.rows)
        for row in range(self.cols):
            for col in range(self.rows):
                mtrx.set_value(row, col, self.get_value(col, row))
        return mtrx

    def __round__(self, ndigits=0):
        mtrx = Matrix(self.rows, self.cols)
        for row in range(mtrx.rows):
            for col in range(mtrx.cols):
                mtrx.set_value(row, col, round(self.get_value(row, col), ndigits))
        return mtrx
    
    