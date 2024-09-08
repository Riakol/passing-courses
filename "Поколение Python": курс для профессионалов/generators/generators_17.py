import datetime

def years_days(year):
    for month in range(1, 13):
        for day in range(1, 32):
            try:
                date = datetime.date(year, month, day)
                yield date
            except ValueError:
                continue