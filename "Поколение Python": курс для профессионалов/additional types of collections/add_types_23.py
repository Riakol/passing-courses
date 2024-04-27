# put your python code here
books = [int(i) for i in input().split()]
total = 0

for i in range(int(input())):
    customers = tuple(map(int, input().split()))
    if customers[0] in books:
        total += customers[1]
        del books[books.index(customers[0])]
print(total)
