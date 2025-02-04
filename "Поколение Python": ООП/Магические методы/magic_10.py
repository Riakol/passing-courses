from functools import total_ordering


@total_ordering
class Month:
    def __init__(self, year, month) -> None:
        self.year = year
        self.month = month

    def __repr__(self) -> str:
        return f"Month({self.year}, {self.month})"
    
    def __str__(self) -> str:
        return f"{self.year}-{self.month}"
    
    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, Month):
            return self.year == __value.year and self.month == __value.month
        elif isinstance(__value, tuple):
            return (self.year, self.month) == __value
        return NotImplemented
    
    def __gt__(self, __value: object) -> bool:
        if isinstance(__value, Month):
            return self.year > __value.year or (self.year == __value.year and self.month > __value.month)
        elif isinstance(__value, tuple):
            return (self.year, self.month) > __value or (self.year == __value[0] and self.month > __value[1])
        return NotImplemented
    
