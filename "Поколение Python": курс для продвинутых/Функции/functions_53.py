# put your python code here
ip_list = [input() for _ in range(int(input()))]

def ip(x):
    total = 0
    powers = len(x.split('.')) - 1
    for i in x.split('.'):
        total += int(i) * 256**powers
        powers -= 1
    return total
        
for i in sorted(ip_list, key=ip):
    print(i)
