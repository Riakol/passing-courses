# put your python code here
import string
password = input()

print(['NO', 'YES'][all([any(i for i in password if i in string.digits),any(i for i in password if i in string.ascii_uppercase), any(i for i in password if i in string.ascii_lowercase), len(password) >= 7])])
