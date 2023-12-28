my_file = open('prices.txt', 'r', encoding='utf-8')
content = my_file.readlines()

total = 0
for i in content:
    total += int(i.split()[1]) * int(i.split()[2])

print(total)

my_file.close()
