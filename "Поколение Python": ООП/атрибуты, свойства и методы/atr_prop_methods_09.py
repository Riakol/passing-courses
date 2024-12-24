class Gun:
    def __init__(self):
        self.x = 0

    def shoot(self):
        if self.x % 2 == 0:
            print("pif")
            self.x += 1
        else:
            print("paf")
            self.x += 1

