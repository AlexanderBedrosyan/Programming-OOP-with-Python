class Person:

    def __init__(self, name:str, surname:str):
        self.name = name
        self.surname = surname

    def __repr__(self):
        return f"{self.name} {self.surname}"

    def __add__(self, other):
        return Person(self.name, other.surname)


class Group:

    def __init__(self, name: str, people: list):
        self.name = name
        self.people = people
        self.__counter = 0

    def __len__(self):
        return len(self.people)

    def __add__(self, other):
        new_name = f"{self.name} {other.name}"
        new_list = self.people + other.people
        return Group(new_name, new_list)

    def __repr__(self):
        return f"Group {self.name} with members {', '.join(str(ch) for ch in self.people)}"

    def __getitem__(self, index):
        return f"Person {index}: {self.people[index].name} { self.people[index].surname}"

    def __iter__(self):
        return self

    def __next__(self):
        self.__counter += 1
        if (self.__counter - 1) == len(self.people):
            raise StopIteration
        else:
            return f"Person {self.__counter - 1}: {self.people[self.__counter - 1].name} {self.people[self.__counter - 1].surname}"


p0 = Person('Aliko', 'Dangote')
p1 = Person('Bill', 'Gates')
p2 = Person('Warren', 'Buffet')
p3 = Person('Elon', 'Musk')
p4 = p2 + p3

first_group = Group('__VIP__', [p0, p1, p2])
second_group = Group('Special', [p3, p4])
third_group = first_group + second_group

print(len(first_group))
print(second_group)
print(third_group[0])

for person in third_group:
    print(person)
