# put your python code here
def parabola(a, b, c):
    return ((-(b/(2*a)), (((4*a*c)-b**2))/4/a))

a, b, c = int(input()), int(input()), int(input())
print(parabola(a,b,c))
