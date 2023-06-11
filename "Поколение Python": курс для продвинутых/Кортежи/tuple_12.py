tuples = [(), (), ('',), ('a', 'b'), (), ('a', 'b', 'c'), (1,), (), (), ('d',), ('', ''), ()]
non_empty_tuples = []

for i in range(len(tuples)):
    if tuples[i]:
        non_empty_tuples.append(tuples[i])
print(non_empty_tuples)
