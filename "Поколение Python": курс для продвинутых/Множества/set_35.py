# put your python code here
first_listik = input()
second_listik = input()

if set(first_listik.split()) & set(second_listik.split()):
    print(*sorted(set(first_listik.split()) & set(second_listik.split()), reverse=True, key=int))
else:
    print('BAD DAY')