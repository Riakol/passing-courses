# put your python code here
import re

def are_coordinates(xy):
    res = re.sub(r'\(|\)', r'', xy)
    return True if -90 <= float(res.split(',')[0]) <= 90 and -180 <= float(res.split(',')[1]) <= 180 else False

coordinates = [are_coordinates(x.strip()) for x in open(0)]
print(*coordinates, sep='\n')

