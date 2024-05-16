def triangle(n):
    def inner_triangle(x):
        if x <= n:
            print('*' * x)
            inner_triangle(x + 1)
    inner_triangle(1)
