class Pet:
    all_pets = []

    def __init__(self, name=None) -> None:
        self.name = name
        self.__class__.all_pets.append(self)


    @classmethod
    def first_pet(cls):
        if not cls.all_pets:
            return None
        return cls.all_pets[0]

    @classmethod
    def last_pet(cls):
        if not cls.all_pets:
            return None
        return cls.all_pets[-1]

    @classmethod
    def num_of_pets(cls):
        return len(cls.all_pets)


