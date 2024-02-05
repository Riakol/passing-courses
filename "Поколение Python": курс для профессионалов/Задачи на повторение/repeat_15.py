n = [i for i in range(1, int(input()) + 1)]
my_dict = dict()

for i in n:
    if str(sum(map(int, str(i)))) in my_dict.keys():
        my_dict[str(sum(map(int, str(i))))].append(i)
    else:
        my_dict[str(sum(map(int, str(i))))] = [i]

print(len(max(my_dict.values(), key=len)))
