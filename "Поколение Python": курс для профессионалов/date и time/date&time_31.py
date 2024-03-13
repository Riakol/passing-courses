from datetime import date

dates = input().split()
output = []

if len(dates) > 1:
    for i in range(1, len(dates)):
        d, m, y = map(int, dates[i].split('.'))
        d1, m1, y1 = map(int, dates[i-1].split('.'))
        output.append(abs(date(day=d, month=m,year=y) - date(day=d1, month=m1,year=y1)).days)
    print(output)
else:
    print([])
