from datetime import date 

def get_date_range(start, end):
    return list(map(lambda x: date.fromordinal(x), range(start.toordinal(), end.toordinal() + 1)))
