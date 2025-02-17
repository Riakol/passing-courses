class Queue:
    def __init__(self, *args) -> None:
        self.args = [*args]

    def add(self, *other):
        self.args += [x for x in other]

    def pop(self):
        if self.args:
            temp = self.args[0]
            del self.args[0]
            return temp
        return None
    
    def __str__(self) -> str:
        return f"{' -> '.join(str(x) for x in self.args)}"

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return len(self.args) == len(other.args) and all([x == y for x, y in zip(self.args, other.args)])

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return f"{' -> '.join(str(x) for x in (self.args + other.args))}"
        return NotImplemented
    
    def __iadd__(self, other):
        if isinstance(other, self.__class__):
            self.args += other.args
            return self
        return NotImplemented

    def __rshift__(self, n):
        if isinstance(n, int):
            if n >= len(self.args):
                return ''
            else:
                return f"{' -> '.join(str(x) for x in self.args[n:])}"
        return NotImplemented

