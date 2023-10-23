# put your python code here
from fractions import  Fraction as F

n = int(input())
res = 0

for i in range(1, n + 1):
    res += F(1, i**2)
print(res)