class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"
    
    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, Vector):
            return self.x == __value.x and self.y == __value.y
        elif isinstance(__value, tuple):
            return (self.x, self.y) == __value
        return NotImplemented

