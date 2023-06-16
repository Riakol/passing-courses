reference = set(str(i) for i in range(10))
sum_strs = set((input() + input()))

if sum_strs == reference:
    print('YES')
else:
    print('NO')
    