with open(input(), encoding='utf-8') as exam:
    data = exam.read().split('\n')
    checker = 0

    for i in range(len(data)):
        if data[i].startswith('def ') and not data[i-1%len(data)].startswith('# '):
            print(data[i][4:data[i].index('(')])
            checker += 1
    else:
        if checker == 0:
            print('Best Programming Team')
