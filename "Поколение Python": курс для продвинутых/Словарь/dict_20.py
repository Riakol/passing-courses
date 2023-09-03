# put your python code here
phones_book = {}
for i in range(int(input())):
    a, b = input().split()
    phones_book.setdefault(b, []).append(a)

name_in_book = [input().title() for _ in range(int(input()))]

for i in name_in_book:
    if i in phones_book:
        print(*phones_book[i])
    else:
        print('абонент не найден')