# put your python code here
m = int(input())

students = [{input() for _ in range(int(input()))} for _ in range(m)]
visited = sorted(set.intersection(*students), reverse=False)

for i in visited:
    print(i)