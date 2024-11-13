# put your python code here
import sys, re

data = [line.strip() for line in sys.stdin]
template = r'_\d{1,}[A-Za-z]*_?'

for login in data:
    match = re.fullmatch(template, login)
    print(True) if match else print(False)

