from collections import defaultdict

def best_sender(msg, sndrs):
    messanger = defaultdict(int)
    for s, m in zip(senders, messages):
        messanger[s] += len(m.split())
    return max(messanger.items(), key=lambda x: (x[1], x[0]))[0]
