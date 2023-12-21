# put your python code here
n = int(input())

words = [input() for _ in range(n)]

sortered = sorted(words)

def redc(x):
    total = 0
    for i in x:
        total += ord(str(i).upper()) - ord('A')
    return total

for i in sorted(sortered, key=redc):
    print(i)
