# put your python code here
transform = {'execute': 'X', 'write': 'W', 'read': 'R'}
files = {}

for i in range(int(input())):
    name, *operations = input().split()
    files[name] = operations

for i in range(int(input())):
    operation, name  = input().split()
    if transform[operation] in files[name]:
        print('OK')
    else:
        print('Access denied')