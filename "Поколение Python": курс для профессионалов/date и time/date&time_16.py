# put your python code here
from datetime import date

def is_correct(dates):
    try:
        day, month, year = dates.split('.')
        return bool(date(int(year), int(month), int(day)))
    except:
        return False

inp = input()
total = 0


while inp != 'end':
    if is_correct(inp):
        print('Корректная')
        total += 1
    else:
        print('Некорректная')
    inp = input()
print(total)
