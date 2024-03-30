import calendar
from datetime import date

def get_days_in_month(year, month):
    dt = date(year=int(year), month=list(calendar.month_name).index(month), day=1)
    return [date.fromordinal(i) for i in range(dt.toordinal(), dt.toordinal() + calendar.monthrange(int(year), list(calendar.month_name).index(month))[1])]
