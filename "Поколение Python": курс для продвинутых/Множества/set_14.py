text = input().lower()
symbols = set()
text_edited = ''

for i in range(len(text)):
    if text[i] in ".,;:-?!":
        continue
    else:
        text_edited += text[i]

for i in text_edited.split():
    symbols.add(i)
print(len(symbols))
