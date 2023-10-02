from random import *

ticket = []

while len(ticket) != 7:
    rnd = randint(1, 49)
    if rnd not in ticket:
        ticket.append(rnd)

print(*sorted(ticket))