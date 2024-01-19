with open(input(), encoding='utf-8') as rewrite, open('forbidden_words.txt', encoding='utf-8') as forbidden_words:
    bad_w = forbidden_words.read().split()
    text = rewrite.read()
    s_lower = text.lower()
    temp = ''

    for i in bad_w:
        if i in text.lower():
            s_lower = s_lower.replace(i, '*'*(len(i)))
    
    for i, j in zip(s_lower, text):
        if i.startswith('*'):
            temp += i
        else:
            temp += j
    print(temp)
