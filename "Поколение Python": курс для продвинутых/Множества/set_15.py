text = input().split()
similliar = set()

for i in text:
    if i.lstrip('0') in similliar:
        print('YES')
    else:
        similliar.add(i.lstrip('0'))
        print('NO')
