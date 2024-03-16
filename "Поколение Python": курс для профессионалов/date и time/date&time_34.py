from datetime import date, time, datetime, timedelta

total = 0
data = [('07:14', '08:46'),
        ('09:01', '09:37'),
        ('10:00', '11:43'),
        ('12:13', '13:49'),
        ('15:00', '15:19'),
        ('15:58', '17:24'),
        ('17:57', '19:21'),
        ('19:30', '19:59')]

for i in data:
    s, e = [datetime.strptime(x, '%H:%M') for x in i]
    total += (e - s).total_seconds()
print(int(total // 60))
