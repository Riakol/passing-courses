sqr = int(input())
arr = [list(map(int, input().split())) for _ in range(sqr)]
counter = 0
            
for j in arr:
    total = sum(j) / len(j)
    for k in j:
        if total < k:
            counter += 1
    print(counter)
    counter = 0