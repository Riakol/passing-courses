with open('text.txt', 'r', encoding='utf-8') as my_file:
    print(my_file.readline()[::-1])
