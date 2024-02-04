numbers = list(map(int, input().split()))
res = set(i for i in numbers if numbers.count(i) > 1)
print(*sorted(list(res)))

