def sum(n):
    if n < 10:
        return n
    else:
        return int(str(n)[0]) + sum(int(str(n)[1:]))
    
print(sum(int(input())))
