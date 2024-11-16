# put your python code here
import sys, re

counter = 0

for word in sys.stdin:
    if re.search(r'(beegeek).*\1', word.strip()):
        counter += 3
    elif re.match(r'beegeek', word.strip()) or re.search(r'.*beegeek$', word.strip()):
        counter += 2
    elif re.search(r'.*beegeek.*', word.strip()):
        counter += 1

print(counter)

