import calendar
from datetime import date

def get_all_mondays(yr):
    months = []
    
    for i in range(1, 13):
        dayz = (calendar.monthrange(int(yr), i))[1]
        for j in range(date(year=yr, month=i, day=1).toordinal(), date(year=yr, month=i, day=dayz).toordinal() + 1):
            if date.fromordinal(j).weekday() == 0:
                months.append(date.fromordinal(j))
    return months
