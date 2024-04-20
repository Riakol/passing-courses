# put your python code here
from collections import Counter

text = Counter(input().lower().split())

print(', '.join([k for k, v in sorted(text.items()) if v == min(text.values())]))
