from datetime import datetime

my_dict = dict()
pattern = '%d.%m.%Y'

for i in range(int(input())):
    *name_surname, dt = input().split()
    my_dict[datetime.strptime(dt, pattern)] = my_dict.get(datetime.strptime(dt, pattern), []) + [' '.join(name_surname)]

if any([j.strftime(pattern) for j in sorted(my_dict.keys()) if len(my_dict[j]) > 1]):
    [print(j.strftime(pattern)) for j in sorted(my_dict.keys()) if len(my_dict[j]) > 1]
else:
    [print(i.strftime(pattern)) for i in sorted(my_dict.keys())]
        