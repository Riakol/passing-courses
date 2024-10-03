# put your python code here
from itertools import groupby

words = {}
for lengths, amount in groupby(sorted(input().split(), key=len), key=len):
    print(f"{lengths} -> {', '.join(sorted(list(amount)))}")