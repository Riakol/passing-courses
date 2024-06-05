# put your python code here
print(''.join(sorted(sorted(input()), key=lambda x: (not x.islower(), not x.isupper(), x.isdigit() and int(x) % 2 == 0))))

