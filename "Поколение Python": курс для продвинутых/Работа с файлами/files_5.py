my_file = open('nums.txt', 'r', encoding='utf-8')
content = my_file.read().split()

print(sum([int(i) for i in content]))

my_file.close()
