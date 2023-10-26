# put your python code here
from fractions import  Fraction as F
from math import  gcd

n = int(input())
doubles = []

for i in range(1, n):
    for j in range(1, n + 1):
        if i < j and (gcd(i, j) == 1 or gcd(i, j) == 0):
            doubles.append(F(i, j))

for i in sorted(doubles):
    print(i)