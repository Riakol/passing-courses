# put your python code here
from collections import Counter

res = Counter([len(i) for i in input().split()])

[print(f"Слов длины {k}: {v}") for k, v in sorted(res.items(), key=lambda x: (x[1]))]
