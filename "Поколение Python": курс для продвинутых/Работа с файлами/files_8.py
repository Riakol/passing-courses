with open('data.txt', 'r', encoding='utf-8') as my_file:
    [print(i.strip()) for i in my_file.readlines()[::-1]]





