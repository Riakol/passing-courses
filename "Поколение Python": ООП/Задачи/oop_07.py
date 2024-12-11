# put your python code here
import calendar
from datetime import datetime

year, month = [int(input()) for _ in range(2)]

calendar.setfirstweekday(calendar.THURSDAY)

if calendar.monthcalendar(year, month)[0][0] == 0:
    dt = datetime(year, month, calendar.monthcalendar(year, month)[4][0])
else:
    dt = datetime(year, month, calendar.monthcalendar(year, month)[3][0])

print(dt.strftime("%d.%m.%Y"))

