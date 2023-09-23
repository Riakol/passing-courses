# put your python code here
text = input().split()
dict_words = {}

for i in text:
    dict_words[i] = dict_words.get(i, 0) + 1
    print(dict_words[i], end=' ')