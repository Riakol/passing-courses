from datetime import datetime

my_dict = dict()
pattern = '%d.%m.%Y'

for i in range(int(input())):
    *name_surname, dt = input().split()
    my_dict[datetime.strptime(dt, pattern)] = my_dict.get(datetime.strptime(dt, pattern), []) + [' '.join(name_surname)]

if len(my_dict[min(my_dict.keys())]) > 1:
    print(f"{min(my_dict.keys()).strftime(pattern)} {len(my_dict[min(my_dict.keys())])}")
else:
    print(f"{min(my_dict.keys()).strftime(pattern)} {my_dict[min(my_dict.keys())][0]}")
