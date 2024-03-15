from datetime import date, datetime, timedelta

pattern = '%H:%M'
start_day, end_day = [datetime.strptime(input(), pattern) for _ in range(2)]

while start_day + timedelta(minutes=45) <= end_day:
    print(f"{start_day.strftime(pattern)} - {(start_day + timedelta(minutes=45)).strftime(pattern)}")
    start_day += timedelta(minutes=45)
    if start_day + timedelta(minutes=10) <= end_day: 
        start_day += timedelta(minutes=10)
