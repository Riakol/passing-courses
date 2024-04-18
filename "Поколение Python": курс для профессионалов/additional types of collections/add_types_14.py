# put your python code here
from collections import Counter

text = Counter(input().split(','))
mx_len = len(max(text, key=len))

for k, v in sorted(text.items()):
    to_unicode = sum([ord(i) for i in k if i.isalpha()])
    print(f"{k:{mx_len}}: {to_unicode} UC x {v} = {to_unicode * v} UC")
