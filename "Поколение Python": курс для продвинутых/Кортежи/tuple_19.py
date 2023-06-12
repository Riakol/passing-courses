# put your python code here
n = int(input())
scoreboard = [[i for i in input().split()] for _ in range(n)]

for i in scoreboard:
    print(*i)

print()

for i in scoreboard:
    if i[1] == '4' or i[1] == '5':
        print(*i)
        