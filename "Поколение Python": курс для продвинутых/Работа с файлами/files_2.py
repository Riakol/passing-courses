my_file = open(f'{input()}')
content = my_file.readlines()
my_file.close()

print(content[-2].rstrip())
