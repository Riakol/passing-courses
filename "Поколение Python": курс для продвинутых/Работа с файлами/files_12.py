with open('file.txt', 'r', encoding='utf-8') as my_file:
    content = my_file.readlines()
    clean_list = list(map(lambda x: [i for i in x if i.isalpha()], [[j.strip(',."') for j in i.strip().split()] for i in content]))
    english_alphabet = sum([sum([len(j) for j in i]) for i in clean_list]) + 1
    words = sum([sum([len(j) for j in i]) for i in [list(map(lambda x: x, [[j.strip(',."') for j in i.strip().split()] for i in content]))]]) 
    print(f"Input file contains:\n{english_alphabet} letters\n{words} words\n{len(clean_list)} lines")