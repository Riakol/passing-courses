class Gun:
    def __init__(self) -> None:
        self.bullets = -1
        self.count = 0

    def shoot(self):
        self.count += 1
        self.bullets += 1
        if self.bullets % 2 == 0:
            print("pif")
        else:
            print("paf")


    def shots_count(self):
        return self.count
    
    def shots_reset(self):
        self.count = 0
        self.bullets = -1
        