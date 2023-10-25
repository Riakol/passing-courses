# put your python code here
from fractions import  Fraction as F
from math import gcd

n = int(input())
doubles = []

for i in range(1, n):
    for j in range(1, n + 1):
        if i < j and i + j == n and gcd(i, j) == 1:
            doubles.append(f"{i}/{j}")

print(F(doubles[-1]))