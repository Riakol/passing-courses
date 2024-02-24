from datetime import date

def print_good_dates(dates):
    [print(date.fromisoformat(str(i)).strftime('%B %d, %Y')) for i in sorted(dates) if i.day + i.month == 29]
