from abc import ABC, abstractmethod

from project import helper


class Musician(ABC):

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.skills = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        message = "Musician name cannot be empty!"
        helper.value_error_if_value_is_empty_string(value, message)
        helper.value_error_if_value_contains_only_white_spaces(value, message)
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        message = "Musicians should be at least 16 years old!"
        helper.value_error_if_number_is_less_than_other_number(value, 16, message)
        self.__age = value

    @abstractmethod
    def available_skills(self):
        pass

    def learn_new_skill(self, new_skill: str):
        if new_skill not in self.available_skills():
            raise ValueError(f"{new_skill} is not a needed skill!")
        if new_skill in self.skills:
            raise Exception(f"{new_skill} is already learned!")
        self.skills.append(new_skill)
        return f"{self.name} learned to {new_skill}."
