from datetime import date

def is_correct(day, month, year):
    try:
        my_date = date(int(year), int(month), int(day))
        return bool(my_date)
    except:
        return False
    