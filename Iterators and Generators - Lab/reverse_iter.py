class reverse_iter:

    def __init__(self, current_list):
        self.current_list = current_list
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == len(self.current_list):
            raise StopIteration
        self.index += 1
        return self.current_list[-self.index]


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
