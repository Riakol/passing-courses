import re, sys

counter = 0

for text in sys.stdin:
    match = re.search(r'beegeek', text.strip(), re.IGNORECASE)
    if match:
        counter += 1

print(counter)