def my_pow(num, res=[]):
    for i, j in enumerate(str(num)):
        res.append(int(j)**(int(i) + 1))
    return sum(res)
