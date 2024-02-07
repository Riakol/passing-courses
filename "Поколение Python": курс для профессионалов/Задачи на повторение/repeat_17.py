ru = 'ауоыиэяюёе'
word = input()
words = [input() for _ in range(int(input()))]
ind, row = [], []

for i in range(len(word)):
    if word[i] in ru:
        ind.append(i)

for i in words:
    for j in range(len(i)):
        if i[j] in ru:
            row.append(j)
    if row == ind:
        print(i)
        row = []
    else:
        row = []
