from datetime import date

days = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
f = date(day=1, month=1, year=1)
s = date(day=31, month=12, year=9999)

for i in range(f.toordinal(), s.toordinal() + 1):
    if date.fromordinal(i).day == 13:
        days[date.fromordinal(i).weekday()] = days.get(date.fromordinal(i).weekday(), 0) + 1

[print(days[i]) for i in days.keys()]
