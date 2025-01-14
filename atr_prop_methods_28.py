class QuadraticPolynomial:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.discriminant = self.b ** 2 - 4 * self.a * self.c

    @property
    def x1(self):
        if self.discriminant < 0:
            return None
        return (-self.b - (self.b**2 - 4 * self.a * self.c) ** 0.5) / (2 * self.a)

    @property
    def x2(self):
        if self.discriminant < 0:
            return None
        return (-self.b + (self.b**2 - 4 * self.a * self.c) ** 0.5) / (2 * self.a)

    @property
    def view(self):
        sign_a = self.a if self.a >= 0 else f'-{abs(self.a)}'
        sign_b = '+' if self.b >= 0 else '-'
        sign_c = '+' if self.c >= 0 else '-'
        return f"{sign_a}x^2 {sign_b} {abs(self.b)}x {sign_c} {abs(self.c)}"

    @property
    def coefficients(self):
        abc = (self.a, self.b, self.c)
        return f"{abc}"

    @coefficients.setter
    def coefficients(self, new_coefficients):
        self.a, self.b, self.c = new_coefficients
        self.discriminant = self.b ** 2 - 4 * self.a * self.c