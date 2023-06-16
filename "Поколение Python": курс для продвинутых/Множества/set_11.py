word = input().split()
model1 = set(word[0])
model2 = set(word[1])
model3 = set(word[2])

if model1 == model2 == model3:
    print('YES')
else:
    print('NO')
    