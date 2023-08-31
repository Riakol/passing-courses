# put your python code here
dict_1, dict_2 = {}, {}

for i in input().split():
    for j in i.strip('.,!?:;-').lower():
        dict_1[j] = dict_1.get(j, 0) + 1

for j in input().split():
    for k in j.strip('.,!?:;-').lower():
        dict_2[k] = dict_2.get(k, 0) + 1

print(['NO', 'YES'][dict_1 == dict_2])