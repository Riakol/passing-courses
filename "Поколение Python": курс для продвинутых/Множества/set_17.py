a = set(int(i) for i in input().split())
b = set(int(i) for i in input().split())
print(*sorted(*[a&b]))

