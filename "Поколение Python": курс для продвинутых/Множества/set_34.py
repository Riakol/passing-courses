# put your python code here
m, n = [int(input()) for _ in range(2)]
books_on_library = [input() for _ in range(m)]
summer_books = [input() for _ in range(n)]

for i in summer_books:
    if i in books_on_library:
        print('YES')
    else:
        print('NO')