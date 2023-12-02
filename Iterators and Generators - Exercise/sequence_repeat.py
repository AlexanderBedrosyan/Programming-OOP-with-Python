from collections import deque

class sequence_repeat:

    def __init__(self, word, number):
        self.word = deque(ch for ch in word)
        self.number = number

    def __iter__(self):
        return self

    def __next__(self):
        if self.number == 0:
            raise StopIteration
        ch = self.word.popleft()
        self.word.append(ch)
        self.number -= 1
        return ch


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')
