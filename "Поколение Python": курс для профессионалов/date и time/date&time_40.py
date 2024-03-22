from datetime import datetime, timedelta

my_dict = dict()
pattern = '%d.%m.%Y'
current_dt = datetime.strptime(input(), pattern) + timedelta(days=1)

for i in range(int(input())):
    *name_surname, dt = input().split()
    for i in range(current_dt.toordinal(), current_dt.toordinal() + 7):
        if datetime.fromordinal(i).day == datetime.strptime(dt, pattern).day and datetime.fromordinal(i).month == datetime.strptime(dt, pattern).month:
            my_dict[datetime.strptime(dt, pattern)] = my_dict.get(datetime.strptime(dt, pattern), []) + [' '.join(name_surname)]
            break

if my_dict:
    print(*my_dict[max(my_dict.keys())])
else:
    print('Дни рождения не планируются')
