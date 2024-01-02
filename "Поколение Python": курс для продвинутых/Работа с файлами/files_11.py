with open('nums.txt', 'r', encoding='utf-8') as my_file:
    content = my_file.readlines()
    total = 0
    for k in [[j for j in i.split()] for i in content]:
        row = ''
        for z in str(k):
            if z.isdigit():
                row += z
            else:
                if not row:
                    continue
                else:
                    total += int(row)
                    row = ''
    print(total)
