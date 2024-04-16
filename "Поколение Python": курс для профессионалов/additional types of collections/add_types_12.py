from collections import Counter

def count_occurences(count, iterations):
    nus = Counter(iterations.lower().split())
    return nus[count.lower()]
