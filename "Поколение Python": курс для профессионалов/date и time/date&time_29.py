from datetime import date

def num_of_sundays(yar):
    return date(year=yar, month=12, day=31).strftime('%U')
