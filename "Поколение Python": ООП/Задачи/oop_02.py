# put your python code here
def is_correct_bracket(text):
    counter = 0
    for sym in text:
        counter = counter + 1  if sym == '(' else counter - 1
        if counter < 0:
            return False
    return counter == 0

txt = input()

print(is_correct_bracket(txt))

