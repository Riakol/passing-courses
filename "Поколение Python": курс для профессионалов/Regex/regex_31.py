# put your python code here
import sys, re

data = [line.strip() for line in sys.stdin]
template = r'(\d{1,3})([ -])(\d{1,3})\2(\d{4,10})'

for number in data:
    match = re.fullmatch(template, number)
    if match:
        print(f'Код страны: {match.group(1)}, Код города: {match.group(3)}, Номер: {match.group(4)}')

