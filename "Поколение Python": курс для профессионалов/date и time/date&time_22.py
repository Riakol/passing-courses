from datetime import datetime

with open('diary.txt', 'r', encoding='utf-8') as text:
    data = sorted(text.read().split('\n\n'), key=lambda x: datetime.strptime(x.split('\n')[0], '%d.%m.%Y; %H:%M'))
    [print(f"{i}\n") for i in data]
    