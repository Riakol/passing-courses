with open('files.txt', encoding='utf-8') as data:
    content = data.read().split('\n')[:-1]
    modules = []
    check = 0
    exts = {'B': 0, 'KB': 0, 'MB': 0, 'GB': 0}
    for i in sorted(content, key=lambda x: x.split()[0].split('.')[1]):
        extension = i.split()[0].split('.')[1]
        count = sum(1 for line in sorted(content, key=lambda x: x.split()[0].split('.')[1]) if line.split()[0].split('.')[1] == extension)
        name, size_num, size_bite = i.split()
        exts[size_bite] = exts.get(size_bite, 0) + int(size_num)
        modules.append(name)
        check += 1
        if check == count:
            row, empty = [], {'B', 'KB', 'MB', 'GB'}
            for k, v in exts.items():
                if v:
                    row.append(k)
            asd = sorted(list(empty - set(row)), key=lambda x: row[-1])
            if len(row) == 1:
                if exts[row[0]] >= 1024:
                    print(*sorted(modules), sep='\n')
                    print(f"{'-'*10}\nSummary: {round(exts[row[0]] / 1024)} {asd[-1]}\n")
                    modules = []
                else:
                    print(*sorted(modules), sep='\n')
                    print(f"{'-'*10}\nSummary: {exts[row[0]]} {row[0]}\n")
                    modules = []
                exts = {'B': 0, 'KB': 0, 'MB': 0, 'GB': 0}
                check = 0
            if len(row) == 2:
                exts[row[0]] += round(exts[row[-1]] * 1024)
                print(*sorted(modules), sep='\n')
                print(f"{'-'*10}\nSummary: {round(exts[row[0]] / 1024)} {row[-1]}\n")
                exts = {'B': 0, 'KB': 0, 'MB': 0, 'GB': 0}
                check = 0
                modules = []
            if len(row) == 3:
                exts[row[1]] += round(exts[row[-1]] * 1024)
                exts[row[0]] += round(exts[row[1]] * 1024)
                print(*sorted(modules), sep='\n')
                print(f"{'-'*10}\nSummary: {round(exts[row[0]] / 1024 / 1024)} {row[-1]}\n")
                exts = {'B': 0, 'KB': 0, 'MB': 0, 'GB': 0}
                check = 0
                modules = []
                