def print_products(*args):
    cnt = 0
    for e in args:
        if type(e) == str and e:
            cnt += 1
            print(f'{cnt}) {e}')
    if cnt == 0:
        print('Нет продуктов')
