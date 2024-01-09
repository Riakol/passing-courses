# put your python code here
with open('input.txt', 'r', encoding='utf-8') as inp, open('output.txt', 'w', encoding='utf-8') as out:
    inp_data = inp.read().split('\n')
    [out.write(f"{i + 1}) {item}\n") for i, item in enumerate(inp_data)]
