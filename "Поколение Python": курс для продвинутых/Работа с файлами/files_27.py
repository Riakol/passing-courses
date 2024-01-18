with open(input(), encoding='utf-8') as exam:
    data = exam.read().split('\n')
    for i in data[-10:]:
        print(i)
