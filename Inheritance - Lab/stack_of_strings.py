class Stack:

    def __init__(self):
        self.data: list = []

    def push(self, element):
        self.data.append(element)

    def pop(self):
        ch = self.data.pop()
        return ch

    def top(self):
        return self.data[-1]

    def is_empty(self):
        if not self.data:
            return True
        return False

    def __str__(self):
        return '[' + ', '.join(self.data[::-1]) + ']'