from random import shuffle, randint

list_of_students = [input() for _ in range(int(input()))]
previous = ''
indx = 0

while indx != len(list_of_students):
    rnd = randint(0, len(list_of_students) - 1)
    if list_of_students[indx] != list_of_students[rnd] and str(rnd) not in previous:
        print(f"{list_of_students[indx]} - {list_of_students[rnd]}")
        indx += 1
        previous += str(rnd)