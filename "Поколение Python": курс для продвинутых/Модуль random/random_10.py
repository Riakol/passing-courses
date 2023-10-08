# put your python code here
from random import randint as ri, shuffle

counter = 1
matrix = [i for i in range(1, 75)]
shuffle(matrix)

for i in range(5):
    for j in range(5):
        if counter == 13:
            counter += 1
            print(str(0).ljust(3), end=' ')
        else:
            print(str(matrix[counter]).ljust(3), end=' ')
            counter += 1
    print()