from datetime import date

dates = [date.fromisoformat(input()) for _ in range(int(input()))]

[print(i.strftime('%d/%m/%Y')) for i in sorted(dates)]
