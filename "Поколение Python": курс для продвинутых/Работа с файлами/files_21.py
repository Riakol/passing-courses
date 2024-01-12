# put your python code here
for i in range(int(input())):
    with open(input(), 'r', encoding='utf-8') as inp, open('output.txt', 'a', encoding='utf-8') as output:
        data = inp.read()
        [output.write(i) for i in data]
