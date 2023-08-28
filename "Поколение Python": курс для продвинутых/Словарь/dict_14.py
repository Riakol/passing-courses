# put your python code here
symbols = input().split()
result = []

for i in symbols:
    if i not in result:
        result.append(i)
        print(i, end=' ')
    else:
        result.append(f"{i}_{result.count(i)}")
        coubter = result.count(f"{i}_{result.count(i)}")
        print(f"{i}_{coubter}", end=' ')