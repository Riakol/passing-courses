class Todo:
    def __init__(self, things=[]) -> None:
        self.things = things
        self.low = 0
        self.high = 0

    def add(self, business, priority):
        self.things.append((business, priority))
        self.low = min([i[1] for i in self.things]) if self.things else []
        self.high = max([i[1] for i in self.things]) if self.things else []

    def get_by_priority(self, n):
        return list(map(lambda x: x[0], filter(lambda x: x[1] == n, self.things))) if self.things else []

    def get_low_priority(self):
        return [i[0] for i in self.things if i[1] == self.low]

    def get_high_priority(self):
        return [i[0] for i in self.things if i[1] == self.high]
    
    