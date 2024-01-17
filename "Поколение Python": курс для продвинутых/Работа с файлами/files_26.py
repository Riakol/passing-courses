with open('words.txt', encoding='utf-8') as exam:
    largest = 14
    data = exam.read().split()
    for i in data:
        if len(i) >= largest:
            largest = len(i)
            print(i)
