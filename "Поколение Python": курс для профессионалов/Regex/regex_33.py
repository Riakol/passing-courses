# put your python code here
import sys, re

[print(word.strip()) for word in sys.stdin if re.fullmatch(r'(\w+)\1', word.strip())]
