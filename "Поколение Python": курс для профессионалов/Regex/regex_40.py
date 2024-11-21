# put your python code here
import re

text, word = [input() for _ in range(2)]
pattern = re.escape(word)
matches = re.findall(rf'\b{pattern}\b', text)

print(len(matches))

