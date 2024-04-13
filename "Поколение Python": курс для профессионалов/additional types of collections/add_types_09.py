from collections import defaultdict

def flip_dict(iterations):
    flip = defaultdict(list)

    for k in iterations:
        for j in iterations[k]:
            flip[j].append(k)
    return flip
