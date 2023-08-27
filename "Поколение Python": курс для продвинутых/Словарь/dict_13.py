# put your python code here
text = input()
text_edited = [word.strip(".,!?:;-") for word in text.lower().split()]
min_in_text = min([text_edited.count(i) for i in text_edited])
result = {}

for i in text_edited:
    if text_edited.count(i) == min_in_text:
        result[i] = result.get(i, 0) + 1
print(sorted(result.keys())[0])