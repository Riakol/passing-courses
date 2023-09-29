from random import *

n = int(input())
moneta = {0: 'Орел', 1: 'Решка'}

for i in range(n):
    print(moneta[randint(0, 1)])