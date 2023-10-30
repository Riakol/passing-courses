def matrix(n=None, m=None, value=0):
    if n == None and m == None:        
        return [[value] * 1 for _ in range(1)]
    elif m == None:
        return [[value] * n for _ in range(n)]
    elif value == 0:
        return [[value] * m for _ in range(n)]
    else:
        return [[value] * m for _ in range(n)]