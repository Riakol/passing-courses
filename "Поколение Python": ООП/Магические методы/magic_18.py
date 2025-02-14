class SuperString:
    def __init__(self, string) -> None:
        self.string = string

    def __str__(self) -> str:
        return self.string
    
    def __add__(self, other):
        if isinstance(other, SuperString):
            return SuperString(self.string + other.string)
        return NotImplemented
    
    def __mul__(self, n):
        if isinstance(n, int):
            return SuperString(self.string * n)
        return NotImplemented
    
    def __rmul__(self, n):
        return self.__mul__(n)

    def __truediv__(self, n):
        if isinstance(n, int):
            return SuperString(self.string[:len(self.string) // n])
        return NotImplemented
    
    def __lshift__(self, n):
        if isinstance(n, int):
            if n >= len(self.string):
                return SuperString('')
            if n == 0:
                return SuperString(self.string)
            return SuperString(self.string[:-n])
        return NotImplemented
    
    def __rshift__(self, n):
        if isinstance(n, int):
            if n >= len(self.string):
                return SuperString('')
            return SuperString(self.string[n:])
        return NotImplemented
    
    