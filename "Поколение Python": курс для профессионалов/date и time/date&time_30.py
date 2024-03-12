from datetime import date,timedelta

d, m, y = map(int, input().split('.'))
dt = date(year=y, day=d, month=m)
temp = dt

print(temp.strftime('%d.%m.%Y'))
for i in range(2, 11):
    temp += timedelta(days=i)
    print(temp.strftime('%d.%m.%Y'))
