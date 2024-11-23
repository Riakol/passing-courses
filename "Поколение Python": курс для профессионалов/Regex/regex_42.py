# put your python code here
import re

word, text = input(), input()

matches = re.findall(rf'\b{word[:-2]}u?r\b', text, flags=re.IGNORECASE)

print(len(matches))

