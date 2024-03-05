from datetime import datetime

def is_available_date(booked_dates, date_for_booking):
    if '-' not in date_for_booking:
        dfb = datetime.strptime(date_for_booking, '%d.%m.%Y').date().toordinal()
        for i in booked_dates:
            if len(i) > 10:
                start_date = datetime.strptime(i.split('-')[0], '%d.%m.%Y').date().toordinal()
                end_date = datetime.strptime(i.split('-')[1], '%d.%m.%Y').date().toordinal() + 1
                if dfb in range(start_date, end_date):
                    return False
            else:
                bd = datetime.strptime(i, '%d.%m.%Y').date().toordinal()
                if dfb == bd:
                    return False
        return True
    else:
        dfb_ = [datetime.strptime(i, '%d.%m.%Y').date().toordinal() for i in date_for_booking.split('-')]
        for i in booked_dates:
            if len(i) > 10:
                start_date = datetime.strptime(i.split('-')[0], '%d.%m.%Y').date().toordinal()
                end_date = datetime.strptime(i.split('-')[1], '%d.%m.%Y').date().toordinal() + 1
                for k in range(dfb_[0], dfb_[1] + 1):
                    if k in range(start_date, end_date):
                        return False
            else:
                bd = datetime.strptime(i, '%d.%m.%Y').date().toordinal()
                sd = dfb_[0]
                ed = dfb_[1]
                if bd in range(sd, ed + 1):
                    return False
        return True
    