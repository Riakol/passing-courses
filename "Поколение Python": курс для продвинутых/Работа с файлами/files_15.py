with open('data.csv', 'r', encoding='utf-8') as data:
    keys = data.readline().strip('\n').split(',')
    content = [i.replace('\n', '').split(',') for i in data.readlines()]

    def read_csv():
        return [{x: y for x, y in zip(keys, content[i])} for i in range(len(content))]
        