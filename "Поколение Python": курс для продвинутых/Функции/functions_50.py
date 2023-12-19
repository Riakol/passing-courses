from operator import *

kw = {"+" : add,
       "-" : sub,
       "*" : mul,
       "/" : truediv}

def arithmetic_operation(operation):
    return kw[operation]
