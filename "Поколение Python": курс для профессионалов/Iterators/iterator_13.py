class BoundedRepeater:
    def __init__(self, obj, times) -> None:
        self.obj = obj
        self.times = times
        self.count = -1

    def __iter__(self):
        return self
    
    def __next__(self):
        self.count += 1
        if self.count == self.times:
            raise StopIteration
        return self.obj