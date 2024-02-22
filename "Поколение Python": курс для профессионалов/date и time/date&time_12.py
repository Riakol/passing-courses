from datetime import date

year, month, day = input().split('-')
year2, month2, day2 = input().split('-')

date1 = date(int(year), int(month), int(day))
date2 = date(int(year2), int(month2), int(day2))

minimal = min(date1, date2)

print(minimal.strftime('%d-%m (%Y)'))
