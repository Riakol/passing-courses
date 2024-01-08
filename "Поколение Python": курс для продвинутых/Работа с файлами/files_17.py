# put your python code here
from random import randint as ri

with open('random.txt', 'x', encoding='utf-8') as random_out:
    my_list = [f"{ri(111, 777)}\n" for _ in range(25)]
    random_out.writelines(my_list)
