from abc import ABC, abstractmethod
from project import helper


class Movie(ABC):

    def __init__(self, title: str, year: int, owner: object, age_restriction: int):
        self.title = title
        self.year = year
        self.owner = owner
        self.age_restriction = age_restriction
        self.likes: int = 0

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        message = "The title cannot be empty string!"
        helper.value_error_if_value_is_empty_string(value, message)
        self.__title = value

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        message = "Movies weren't made before 1888!"
        helper.value_error_if_number_is_less_than_other_number(value, 1888, message)
        self.__year = value

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):
        if value.__class__.__name__ != "User":
            raise ValueError("The owner must be an object of type User!")
        self.__owner = value

    @abstractmethod
    def details(self):
        pass