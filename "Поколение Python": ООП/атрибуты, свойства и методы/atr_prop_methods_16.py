class Postman:
    def __init__(self, delivery_data=[]) -> None:
        self.delivery_data = delivery_data
        self.houses = []
        self.flats = []

    def add_delivery(self, st, house, apt):
        self.delivery_data.append((st, house, apt))

    def get_houses_for_street(self, st):
        for i in self.delivery_data:
            if i[0] == st and i[1] not in self.houses:
                self.houses.append(i[1])
        return self.houses
    
    def get_flats_for_house(self, st, house):
        for i in self.delivery_data:
            if (i[0] == st and i[1] == house) and i[2] not in self.flats:
                self.flats.append(i[2])
        return self.flats




