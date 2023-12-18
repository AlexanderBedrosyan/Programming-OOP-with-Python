from abc import ABC, abstractmethod
from project import helper


class Meal(ABC):

    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        message = "Name cannot be an empty string!"
        helper.value_error_if_value_is_empty_string(value, message)
        self.__name = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        message = "Invalid price!"
        helper.value_error_if_number_is_less_than_other_number(value, 0.00, message)
        helper.value_error_if_number_is_equal_to_other_number(value, 0.00, message)
        self.__price = value

    @abstractmethod
    def details(self):
        pass
