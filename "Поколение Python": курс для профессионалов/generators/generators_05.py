from datetime import date

def dates(start, count=None):
    x = 0
    while x != count:
        for i in range(date.toordinal(start) + x, date.toordinal(start) + x + 1):
            x += 1
            try:
                yield date.fromordinal(i)
            except ValueError:
                return
            except StopIteration:
                return

