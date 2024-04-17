# put your python code here
from collections import Counter

[print(f"{k}: {v}") for k, v in sorted(Counter(input().split(',')).items())]
