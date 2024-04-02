# put your python code here
import string

alphabet = string.ascii_lowercase
x = {}

for i in range(26):
    x[alphabet[i]] = i + 1

f, s = [input() for _ in range(2)]

for j in s.lower():
    print(f[x[j] - 1], end='') if j.isalpha() else print(j, end='')
