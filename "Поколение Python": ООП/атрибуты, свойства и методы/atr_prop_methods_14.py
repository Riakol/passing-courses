class TextHandler:
    def __init__(self) -> None:
        self.collection = []

    def add_words(self, text):
        for i in text.split():
            self.collection.append(i)

    def get_shortest_words(self):
        temp = []
        if self.collection:
            for word in self.collection:
                if len(word) == len(min(self.collection, key=len)):
                    temp.append(word)
                else:
                    continue
            return temp
        else:
            return self.collection

    def get_longest_words(self):
        temp = []
        if self.collection:
            for word in self.collection:
                if len(word) == len(max(self.collection, key=len)):
                    temp.append(word)
                else:
                    continue
            return temp
        else:
            return self.collection