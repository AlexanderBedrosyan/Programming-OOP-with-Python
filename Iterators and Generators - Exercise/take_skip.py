class take_skip:

    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.starting_number = 0
        self.needed_number = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.needed_number == self.count:
            raise StopIteration
        self.starting_number += self.step
        self.needed_number += 1
        return self.starting_number - self.step


numbers = take_skip(2, 6)
for number in numbers:
    print(number)


