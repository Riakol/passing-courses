# put your python code here
import re

print(', '.join(re.split(r'\s*(?:\||&|and|or)\s*', input())))

