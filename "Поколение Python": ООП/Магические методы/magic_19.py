class Time:
    def __init__(self, hours, minutes) -> None:
        self.hours, self.minutes = Time._correct_time(hours, minutes)

    @staticmethod
    def _correct_time(hours, minutes):
        return (hours + minutes // 60) % 24, minutes % 60
        
    def __str__(self) -> str:
        return f"{self.hours:02}:{self.minutes:02}"

    def __add__(self, other):
        if isinstance(other, Time):
            return Time(*Time._correct_time(self.hours + other.hours, self.minutes + other.minutes))
        return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, Time):
            self.hours, self.minutes = Time._correct_time(self.hours + other.hours, self.minutes + other.minutes)
            return self
        return NotImplemented

