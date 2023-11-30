class vowels:

    def __init__(self, word):
        self.word = [letter for letter in word if letter.lower() in 'aueoiy']
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == len(self.word):
            raise StopIteration
        self.index += 1

        return self.word[self.index - 1]
