# put your python code here
import re

text, word = [input() for _ in range(2)]

pattern = re.escape(word)
matches = re.findall(rf'\B{pattern}\B', text)

print(len(matches))

