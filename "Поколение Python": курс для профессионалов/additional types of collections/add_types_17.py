# put your python code here

from collections import Counter

text = Counter(input().lower().split()).most_common()

print(max(text, key=lambda x: (x[1], x[0]))[0])
