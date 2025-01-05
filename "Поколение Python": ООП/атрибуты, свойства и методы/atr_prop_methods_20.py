class User:
    def __init__(self, name, age) -> None:
        self.set_name(name)
        self.set_age(age)

    def get_name(self):
        return self._name
    
    def set_name(self, new_name):
        if not (new_name and isinstance(new_name, str) and new_name.isalpha()):
            raise ValueError("Некорректное имя")
        self._name = new_name

    def get_age(self):
        return self._age
    
    def set_age(self, new_age):
        if not (isinstance(new_age, (int, float)) and new_age in range(0, 111)):
            raise ValueError("Некорректный возраст")  
        self._age = new_age




