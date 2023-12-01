class dictionary_iter:

    def __init__(self, current_dict: dict):
        self.current_dict = current_dict
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == len(self.current_dict):
            raise StopIteration
        self.index += 1
        current_list = list(self.current_dict.keys())
        return current_list[self.index - 1], self.current_dict[current_list[self.index - 1]]


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
