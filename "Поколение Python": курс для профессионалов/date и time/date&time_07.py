from datetime import date 

def saturdays_between_two_dates(start, end):
    if end > start:
        return len(list(filter(lambda x: date.fromordinal(x).weekday() == 5, range(start.toordinal(), end.toordinal() + 1))))
    return len(list(filter(lambda x: date.fromordinal(x).weekday() == 5, range(end.toordinal(), start.toordinal() + 1))))
