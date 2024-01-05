with open('population.txt', 'r', encoding='utf-8') as population:
    popul = population.readlines()
    filtered = list(filter(lambda x: x[0].startswith('G') and int(x[-1]) > 500000, [i.strip('\n').split('\t') for i in popul]))
    [print(i[0]) for i in filtered]
