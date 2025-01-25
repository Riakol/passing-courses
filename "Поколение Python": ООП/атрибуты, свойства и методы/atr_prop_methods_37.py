from datetime import date
from functools import singledispatchmethod

class BirthInfo:

    @singledispatchmethod
    def __init__(self, birth_date):
        raise TypeError("Аргумент переданного типа не поддерживается")

    @__init__.register(date)
    def _from_date(self, birth_date):
        self.birth_date = birth_date

    @__init__.register(str)
    def _from_str(self, birth_date):
        try:
            self.birth_date=date.fromisoformat(birth_date)
        except:
            raise TypeError('Аргумент переданного типа не поддерживается')

    @__init__.register(list)
    @__init__.register(tuple)
    def _from_list_tuple(self, birth_date):
        self.birth_date = date(*birth_date)

    @property
    def age(self):
        return current_age(self.birth_date, date.today())