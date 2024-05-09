import sys

text = [elem.strip('\n') for elem in sys.stdin.readlines()]
res = {'numbers': 0, 'not_nums': 0}


for i in text:
    if '.' in i and i.split('.')[0].isdigit() and i.split('.')[1].isdigit():
        res['numbers'] += float(i)
    elif i.isdigit():
        res['numbers'] += int(i)
    else:
        res['not_nums'] += 1
[print(res[i]) for i in res.keys()]
