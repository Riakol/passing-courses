from random import choice as c

my_file = open('lines.txt', 'r', encoding='utf-8')
my_file_info = my_file.readlines()
my_file.close()

print(c(my_file_info).rstrip())
