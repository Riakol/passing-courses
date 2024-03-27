import calendar

year, month, day = map(int, input().split('-'))
print(list(calendar.day_name)[calendar.weekday(year=year, month=month, day=day)])
