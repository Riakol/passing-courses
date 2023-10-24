# put your python code here
from fractions import  Fraction as F
from math import  factorial

n = int(input())
res = 0

for i in range(1, n + 1):
    res += F(1, factorial(i))
print(res)