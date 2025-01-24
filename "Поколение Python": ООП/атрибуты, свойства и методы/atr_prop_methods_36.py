from functools import singledispatchmethod


class Formatter:

    @singledispatchmethod
    @staticmethod
    def format(obj):
        raise TypeError("Аргумент переданного типа не поддерживается")

    @format.register(int)
    @staticmethod
    def _from_int(obj):
        print(f"Целое число: {obj}")

    @format.register(float)
    @staticmethod
    def _from_int(obj):
        print(f"Вещественное число: {obj}")

    @format.register(tuple)
    @staticmethod
    def _from_int(obj):

        print(f"Элементы кортежа: {', '.join(map(str, obj))}")

    @format.register(list)
    @staticmethod
    def _from_dict(obj):
        print(f"Элементы списка: {', '.join(map(str, obj))}")

    @format.register(dict)
    @staticmethod
    def _from_int(obj):
        print(f"Пары словаря: {', '.join(map(str, obj.items()))}")
        
        