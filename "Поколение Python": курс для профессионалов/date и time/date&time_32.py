from datetime import date, datetime

def fill_up_missing_dates(dates):
  
    n_dates = sorted([datetime.strptime(i, '%d.%m.%Y').date().toordinal() for i in dates])
    return [str(date.fromordinal(i).strftime('%d.%m.%Y')) for i in range(n_dates[0], n_dates[-1] + 1)]
