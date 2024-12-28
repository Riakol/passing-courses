class Numbers:
    def __init__(self) -> None:
        self.collection = []

    def add_number(self, n):
        self.collection.append(n)

    def get_even(self):
        return [i for i in self.collection if i % 2 == 0]

    def get_odd(self):
        return [i for i in self.collection if i % 2 != 0]