# put your python code here
print(*sorted((set(input().split()) & set(input().split())) - set(input().split()), reverse=True, key=int))
