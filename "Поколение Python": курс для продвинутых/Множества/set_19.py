my_numbers = [set(input()) for _ in range(int(input()))]
print(*sorted(set.intersection(*my_numbers)))
