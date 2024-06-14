def numbers_sum(elem):
    '''
Принимает список и возвращает сумму его чисел (int, float),
игнорируя нечисловые объекты. 0 - если в списке чисел нет.
    '''
    return sum([i for i in elem if type(i) == int or type(i) == float])
