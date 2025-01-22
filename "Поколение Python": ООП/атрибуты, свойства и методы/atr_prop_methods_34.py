from functools import singledispatchmethod

class Processor:

    @singledispatchmethod
    @staticmethod
    def process(data):
        raise TypeError('Аргумент переданного типа не поддерживается')
    
    @process.register(int)
    @process.register(float)
    @staticmethod
    def _from_int_float(data):
        return data * 2
    
    @process.register(str)
    @staticmethod
    def _from_str(data):
        return data.upper()

    @process.register(list)
    @staticmethod
    def _from_list_tuple(data):
        return sorted(data)
    
    @process.register(tuple)
    @staticmethod
    def _from_list_tuple(data):
        return tuple(sorted(data))
    