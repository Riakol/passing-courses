n = int(input())

My_dict = [input() for _ in range(n)]
total = []

for i in My_dict:
    for j in i.split(","):
        total.append(j.strip())
 
xcv = sorted(list(filter(lambda x: total.count(x) == n, set(total))), reverse=False)
if not xcv:
    print('Сериал снять не удастся')
else:
    print(', '.join(xcv))
    