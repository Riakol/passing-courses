with open('numbers.txt', 'r', encoding='utf-8') as my_file:
    content = my_file.readlines()
    for i in content:
        print(sum([int(j) for j in i.split()]))
