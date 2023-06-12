numbers = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4), (90, 10))
result = 0
new_numbers = []

for i in range(len(numbers)):
    result = sum(numbers[i]) / len(numbers[i])
    new_numbers.append(result)
    result = 0

print(new_numbers)
