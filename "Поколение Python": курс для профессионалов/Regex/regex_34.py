# put your python code here
import sys, re

count_bee = count_geek = 0

for word in sys.stdin:
    if len(re.findall(r'bee', word.strip())) >= 2:
        count_bee += 1
    if re.search(r'\bgeek\b', word.strip()):
        count_geek += 1
        
print(f'{count_bee}\n{count_geek}')

