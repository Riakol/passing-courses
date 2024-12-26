class Scales:
    def __init__(self) -> None:
        self.right = 0
        self.left = 0

    def add_right(self, kg):
        self.right += kg

    def add_left(self, kg):
        self.left += kg
    
    def get_result(self):
        if self.right == self.left:
            return "Весы в равновесии"
        elif self.right > self.left:
            return "Правая чаша тяжелее"
        else:
            return "Левая чаша тяжелее"



