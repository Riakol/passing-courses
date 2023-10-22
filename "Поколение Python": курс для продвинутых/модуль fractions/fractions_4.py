# put your python code here
from fractions import  Fraction as F

x, y = [input() for _ in range(2)]

print(f"{x} + {y} = {F(x) + F(y)}")
print(f"{x} - {y} = {F(x) - F(y)}")
print(f"{x} * {y} = {F(x) * F(y)}")
print(f"{x} / {y} = {F(x) / F(y)}")