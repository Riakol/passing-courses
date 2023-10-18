# put your python code here
from decimal import *

num = Decimal(input())

print(Decimal.exp(num) + Decimal.ln(num) + Decimal.log10(num) + Decimal.sqrt(num))