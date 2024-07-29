class CardDeck:
    def __init__(self) -> None:
        self.suits = ["пик", "треф", "бубен", "червей"]
        self.ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "валет", "дама", "король", "туз"]
        self.index = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index < 52: 
            suit = self.suits[self.index // 13] 
            rank = self.ranks[self.index % 13] 
            self.index += 1 
            return f"{rank} {suit}" 
        else:
            raise StopIteration 

