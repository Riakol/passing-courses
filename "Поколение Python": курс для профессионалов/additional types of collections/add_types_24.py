from collections import Counter, ChainMap

bread = {'булочка с кунжутом': 15, 'обычная булочка': 10, 'ржаная булочка': 15}
meat = {'куриный бифштекс': 50, 'говяжий бифштекс': 70, 'рыбный бифштекс': 40}
sauce = {'сливочно-чесночный': 15, 'кетчуп': 10, 'горчица': 10, 'барбекю': 15, 'чили': 15}
vegetables = {'лук': 10, 'салат': 15, 'помидор': 15, 'огурцы': 10}
toppings = {'сыр': 25, 'яйцо': 15, 'бекон': 30}
ingridients = ChainMap(bread, meat, sauce, vegetables, toppings)

order = Counter(input().split(','))
total = 0

def measure_length():
    len_order = len(' ' * separate) + len(' ' * 3 + str(max(order.values(), key=int)))
    len_price = len(str(total) + 'p' + ' ' * 6)
    return '-' * len_order if len_order > len_price else '-' * len_price

for k, v in sorted(order.items()):
    separate = len(max(order, key=(len)))
    total += v * ingridients[k]
    print(f"{k:{separate}} x {v}")
print(f"{measure_length()}\nИТОГ: {total}р")
