# put your python code here
with open('class_scores.txt', 'r', encoding='utf-8') as class_score, open('new_scores.txt', 'w', encoding='utf-8') as new_s:
    class_scr = class_score.read().split()
    a = [new_s.write(f"{class_scr[i - 1]} {min(100, int(class_scr[i]) + 5)}\n") for i in range(len(class_scr)) if i % 2 == 1]
