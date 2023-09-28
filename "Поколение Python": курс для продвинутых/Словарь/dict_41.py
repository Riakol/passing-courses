# put your python code here
n = int(input())
goods = {}

for i in range(n):
    text = input().split()
    name = text[0] + ':'
    product = text[1]
    quantity = int(text[2])
    
    if name in goods:
        goods[name][product] = goods[name].get(product, 0) + quantity
    else:
        goods.setdefault(name, {})[product] = quantity

for k, v in sorted(goods.items()):
    print(k)
    for key, val in sorted(v.items()):
        print(key, val)