import calendar
from datetime import date

yr = int(input())
counter = 0

for i in range(1, 13):
    dayz = (calendar.monthrange(int(yr), i))[1]
    for j in range(date(year=yr, month=i, day=1).toordinal(), date(year=yr, month=i, day=dayz).toordinal() + 1):
        if date.fromordinal(j).weekday() == 3:
            counter += 1
        if counter == 3:
            print(date.fromordinal(j).strftime('%d.%m.%Y'))
            counter = 0
            break
