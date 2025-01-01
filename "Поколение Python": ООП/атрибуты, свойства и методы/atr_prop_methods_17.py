class Wordplay:
    def __init__(self, words=[]) -> None:
        self.words = words

    def add_word(self, word):
        if not word in self.words:
            self.words.append(word)

    def words_with_length(self, n):
        return [i for i in self.words if len(i) == n]

    def only(self, *args):
        temp = []
        for i in self.words:
            row = []
            for j in i:
                if j in args:
                    row.append(j)
                else:
                    break
            if row and not ''.join(row) in temp:
                temp.append(''.join(row))
        return temp

    def avoid(self, *args):
        temp = []
        for i in self.words:
            row = []
            for j in i:
                if j not in args:
                    row.append(j)
                else:
                    row = []
                    break
            if row and not ''.join(row) in temp:
                temp.append(''.join(row))
        return temp