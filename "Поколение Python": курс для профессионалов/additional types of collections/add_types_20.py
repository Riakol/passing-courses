from collections import Counter

from collections import Counter

data = Counter('aksjaskfjsklfjdslkfjajfopewtoieqpwdpqworiiqjskanvmcxbmpewrqopkqwlmdzczmxvmvlnjpjqpkqzxvmbowiqeorewi')

data.__dict__['min_values'] = lambda: [(k, v) for k, v in data.items() if v == min(data.values())]
data.__dict__['max_values'] = lambda: [(k, v) for k, v in data.items() if v == max(data.values())]
