# put your python code here
directr = set(input().split())
assistnt = set(input().split())
print(*sorted(directr | assistnt, reverse=False))