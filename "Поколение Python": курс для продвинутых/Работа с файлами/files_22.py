# put your python code here
def minutes(x):
        res=[int(i) for i in x.split(':')]
        return res[0]*60+res[1]

with open('logfile.txt', 'r', encoding='utf-8') as logfile, open('output.txt', 'w', encoding='utf-8') as output:
    for i in logfile:
        name, t1, t2 = i.strip().split(', ')
        if (minutes(t2) - minutes(t1)) >= 60:
            print(name, file=output)
