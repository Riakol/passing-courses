# put your python code here
import re

kwlist = ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

pattern = '|'.join(r'\b' + re.escape(kw) + r'\b' for kw in kwlist)

print(re.sub(rf'{pattern}', r'<kw>', input(), flags=re.IGNORECASE))

