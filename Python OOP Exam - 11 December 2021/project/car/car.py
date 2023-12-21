from abc import ABC, abstractmethod
from project.helper import *


class Car(ABC):

    def __init__(self, model: str, speed_limit: int):
        self.model = model
        self.speed_limit = speed_limit
        self.is_taken = False

    @abstractmethod
    def speed_limit_range(self):
        pass

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        value_error_if_number_is_less_than_other_number(len(value), 4, f"Model {value} is less than 4 symbols!")
        self.__model = value

    @property
    def speed_limit(self):
        return self.__speed_limit

    @speed_limit.setter
    def speed_limit(self, value):
        value_error_if_number_is_less_than_other_number(value, self.speed_limit_range()[0], f"Invalid speed limit! Must be between {self.speed_limit_range()[0]} and {self.speed_limit_range()[1]}!")
        value_error_if_number_is_bigger_than_other_number(value, self.speed_limit_range()[1], f"Invalid speed limit! Must be between {self.speed_limit_range()[0]} and {self.speed_limit_range()[1]}!")
        self.__speed_limit = value
