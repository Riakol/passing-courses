mylist = []
for i in range(int(input())):
    mylist.append(input().lower())
print(len(set(''.join(mylist))))
