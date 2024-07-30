class Cycle:
    def __init__(self, iterable):
        self.iterable = iterable
        self.index = -1

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index + 1 < len(self.iterable):
            self.index += 1
            return self.iterable[self.index]
        self.index = 0
        return self.iterable[self.index]

