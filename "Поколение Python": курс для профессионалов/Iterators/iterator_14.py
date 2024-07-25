class Square:
    def __init__(self, n):
        self.n = n
        self.value = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        self.value += 1
        if self.value - self.n == 1:
            raise StopIteration
        return self.value ** 2

