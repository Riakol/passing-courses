from datetime import datetime, timedelta

pattern = '%d.%m.%Y %H:%M'
is_open = datetime.strptime(input(), pattern)
schedule = {
    0: {'start': timedelta(hours=9), 'end': timedelta(hours=21)},
    1: {'start': timedelta(hours=9), 'end': timedelta(hours=21)},
    2: {'start': timedelta(hours=9), 'end': timedelta(hours=21)},
    3: {'start': timedelta(hours=9), 'end': timedelta(hours=21)},
    4: {'start': timedelta(hours=9), 'end': timedelta(hours=21)},
    5: {'start': timedelta(hours=10), 'end': timedelta(hours=18)},
    6: {'start': timedelta(hours=10), 'end': timedelta(hours=18)}
}

current_time = timedelta(hours=is_open.hour, minutes=is_open.minute)

if current_time >= schedule[is_open.weekday()]['end'] or current_time < schedule[is_open.weekday()]['start']:
    print('Магазин не работает')
else:
    print(int((schedule[is_open.weekday()]['end'] - current_time).total_seconds() / 60))
    