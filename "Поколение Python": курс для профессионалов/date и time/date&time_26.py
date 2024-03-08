from datetime import date, timedelta, datetime

dt = datetime.strptime(input(), '%d.%m.%Y')

print((dt - timedelta(days=1)).strftime('%d.%m.%Y'))
print((dt + timedelta(days=1)).strftime('%d.%m.%Y'))
