class PowerOf:
    def __init__(self, number):
        self.number = number
        self.value = -1

    def __iter__(self):
        return self
    
    def __next__(self):
        self.value += 1
        return self.number ** self.value

