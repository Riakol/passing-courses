from decimal import *

num = Decimal(input())

num_ed = set(num.as_tuple().digits)

for i in str(num)[:str(num).index('.')]:
    if i == '-':
        continue
    num_ed |= {int(i)}

print(max(num_ed) + min(num_ed))