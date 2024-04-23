# put your python code here
from collections import Counter
import sys

data = [line.strip().split() for line in sys.stdin]
res = Counter()

for i in data:
    name, grade = i
    res[name] = int(grade)

print(res.most_common()[-2][0])
