from collections import defaultdict

def wins(pair):
    table = defaultdict(set)
    for i in pair:
        winner, loser = i
        table[winner].add(loser)
    return table
