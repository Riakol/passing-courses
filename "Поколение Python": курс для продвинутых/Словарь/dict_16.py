# put your python code here
dict_1, dict_2 = {}, {}

for i in input():
    dict_1[i] = dict_1.get(i, 0) + 1

for j in input():
    dict_2[j] = dict_2.get(j, 0) + 1

print(['NO', 'YES'][dict_1 == dict_2])