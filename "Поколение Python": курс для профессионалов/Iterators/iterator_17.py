class DictItemsIterator:
    def __init__(self, data: tuple) -> tuple:
        self.data = data
        self.keys = list(data.keys())
        self.index = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index < len(self.data):
            k = self.keys[self.index]
            v = self.data[k]
            self.index += 1
            return (k, v)
        raise StopIteration
        
        