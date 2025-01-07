class HourClock:
    def __init__(self, hours) -> None:
        self.hours = hours

    def get_hours(self):
        return self._hours
    
    def set_hours(self, new_hours):
        if not (isinstance(new_hours, int) and 1 <= new_hours <= 12):
            raise ValueError("Некорректное время")
        self._hours = new_hours
    
    hours = property(get_hours, set_hours)
    