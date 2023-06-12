numbers = (2, 3, 5, 7, -11, 13, 17, 19, 23, 29, 31, -6, 41, 43, 47, 53, 59, 61, -96, 71, 1000, -1)
multi = numbers[0]

for i in range(1):
    for j in range(i + 1, len(numbers)):
        multi *= numbers[j]
print(multi)
