abscissas, ordinates, applicates = [input().split() for _ in range(3)]

print(all(map(lambda x: float(x[0])**2 + float(x[1])**2 + float(x[2])**2 <= 4, zip(abscissas, ordinates, applicates))))





