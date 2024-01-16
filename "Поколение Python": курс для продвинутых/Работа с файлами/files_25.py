with open('grades.txt', encoding='utf-8') as exam:
    data = exam.readlines()
    total = 0
    for i in data:
        name, score1, score2, score3 = i.split()
        if int(score1) >= 65 and int(score2) >= 65 and int(score3) >= 65:
            total += 1
    print(total)
