from random import *

asc = [[65, 90], [97, 122]]
for i in range(int(input())):
    rnd = randint(0, 1)
    print(chr(randint(*asc[rnd])), end='')