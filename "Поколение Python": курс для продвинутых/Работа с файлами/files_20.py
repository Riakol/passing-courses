# put your python code here
with open('goats.txt', 'r', encoding='utf-8') as goats, open('answer.txt', 'w', encoding='utf-8') as anws:
    goats.readline()
    colours = sorted([goats.readline().strip('\n') for _ in range(6)])
    data = goats.read().split('\n')
    goats.readline()
    answer = [anws.write(f"{colours[i]}\n") for i in range((len(colours))) if (data.count(colours[i]) / len(data)) * 100 > 7]
