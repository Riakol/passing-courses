# put your python code here
import re

regex_obj = re.compile(r'\d+')

a, b = map(int, input().split())
text = input()

print(sum(map(int, regex_obj.findall(text, pos=a, endpos=b))))

