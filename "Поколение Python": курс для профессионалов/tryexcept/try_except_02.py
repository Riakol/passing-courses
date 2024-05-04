a, b = [int(input()) for _ in range(2)]
numbers = []

for i in range(a, b + 1):
    if i % 7 == 0:
        numbers.append(i)

print(numbers)