from datetime import datetime

start = datetime.strptime(input(), '%d.%m.%Y')
end = datetime.strptime(input(), '%d.%m.%Y')
gl_dt = None

for x in range(start.toordinal(), end.toordinal() + 1):
    dt = datetime.fromordinal(x)
    if (dt.day + dt.month) % 2 == 1 and (dt.weekday() != 0 and dt.weekday() != 3 or dt.weekday() == 0 or dt.weekday() == 3):
        gl_dt = dt
        break

for j in range(gl_dt.toordinal(), end.toordinal() + 1, 3):
    n_dt = datetime.fromordinal(j)
    if n_dt.weekday() != 0 and n_dt.weekday() != 3:
        print(n_dt.date().strftime('%d.%m.%Y'))
