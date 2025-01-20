class QuadraticPolynomial:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.discriminant = self.b ** 2 - 4 * self.a * self.c

    @classmethod
    def from_iterable(cls, iterable):
        return cls(*iterable)
    
    @classmethod
    def from_str(cls, string):
        test = [float(x) for x in string.split()]
        return cls(*test)

