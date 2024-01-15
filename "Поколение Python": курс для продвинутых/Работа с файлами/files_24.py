from functools import reduce

with open('ledger.txt', encoding='utf-8') as exam:
    data = exam.readlines()
    print('$' + str(reduce(lambda x, y: int(x) + int(y), [i.strip('\n')[1:] for i in data], 0)))
