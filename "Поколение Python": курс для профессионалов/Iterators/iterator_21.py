class Alphabet:
    def __init__(self, language):
        self.language = language
        self.index = -1
        self.alph = {'ru': [chr(i) for i in range(1072, 1104)], 'en': [chr(i) for i in range(97, 123)]}

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.language == 'ru':
            self.index += 1
            return self.alph[self.language][self.index % len(self.alph.get(self.language, []))]
        if self.language == 'en':
            self.index += 1
            return self.alph[self.language][self.index % len(self.alph.get(self.language, []))]
        raise StopIteration
        
        