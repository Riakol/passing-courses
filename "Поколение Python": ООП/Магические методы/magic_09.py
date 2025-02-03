from functools import total_ordering

@total_ordering
class Word:
    def __init__(self, word) -> None:
        self.word = word

    def __str__(self) -> str:
        return f"{self.word.title()}"

    def __repr__(self) -> str:
        return f"Word('{self.word}')"
    
    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, Word):
            return len(self.word) == len(__value.word)
        return NotImplemented
    
    def __gt__(self, __value: object) -> bool:
        if isinstance(__value, Word):
            return len(self.word) > len(__value.word)
        return NotImplemented

