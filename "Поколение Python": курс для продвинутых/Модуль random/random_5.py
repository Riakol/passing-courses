from random import *

def generate_ip():
    ip_adress = ''
    for i in range(4):
        ip_adress += str(randint(0, 255)) + '.'
    return ip_adress[:-1]