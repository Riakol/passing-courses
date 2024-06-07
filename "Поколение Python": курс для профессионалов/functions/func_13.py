# put your python code here
import sys

numbers = [eval(i) for i in sys.stdin.readlines()]

print(max(numbers))
