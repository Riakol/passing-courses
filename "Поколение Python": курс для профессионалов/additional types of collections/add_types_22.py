from collections import Counter

def print_bar_chart(data, mark):
    data_dict = Counter(data)
    m_len = len(max(data_dict, key=len))
    for k, v in sorted(data_dict.items(), key=lambda x: x[1], reverse=True):
        print(f"{k:{m_len}} |{mark * v}")
