# put your python code here
from math import sin

def sqr(x):
    return x**2


def cube(x):
    return x**3


def sqr_(x):
    return x**0.5


def module(x):
    return abs(x)


def sinus(x):
    return sin(x)

num, name = int(input()), input()

my_dict = {'квадрат': sqr, 'модуль': module, 'куб': cube, 'корень': sqr_, 'синус': sinus}

print(my_dict[name](num))