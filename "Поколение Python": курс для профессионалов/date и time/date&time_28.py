from datetime import timedelta, datetime

my_date = datetime.strptime(input(), '%H:%M:%S')
n = int(input())
print((my_date + timedelta(seconds=n)).strftime('%H:%M:%S'))
