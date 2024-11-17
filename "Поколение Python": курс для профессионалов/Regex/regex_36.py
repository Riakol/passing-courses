# put your python code here
import re

match = re.match(r'(Здравствуйте)|(Доброе утро)|(Добрый день)|(Добрый вечер).*', input(), flags=re.IGNORECASE)
print(bool(match))

