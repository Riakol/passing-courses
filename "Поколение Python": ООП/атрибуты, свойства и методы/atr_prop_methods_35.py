from functools import singledispatchmethod

class Negator:

    @singledispatchmethod
    @staticmethod
    def neg(obj):
        raise TypeError("Аргумент переданного типа не поддерживается")
    
    @neg.register(int)
    @neg.register(float)
    def _from_int_float(obj):
        return [abs(obj), -obj][obj > 0]
    
    @neg.register(bool)
    def _from_bool(obj):
        return False if obj else True
    
    