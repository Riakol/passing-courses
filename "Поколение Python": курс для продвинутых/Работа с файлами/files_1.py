my_file = open(f'{input()}', 'r', encoding='utf-8')
content = my_file.read()
print(content)
my_file.close()
