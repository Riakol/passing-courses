# put your python code here
import re

regex_1 = r'7-\d{3}-\d{3}-\d{2}-\d{2}'
regex_2  = r'8-\d{3}-\d{4}-\d{4}'

for elem in input().split():
    if re.findall(regex_1, elem.strip()):
        print(*re.findall(regex_1, elem))
    if re.findall(regex_2, elem.strip()):
        print(*re.findall(regex_2, elem))