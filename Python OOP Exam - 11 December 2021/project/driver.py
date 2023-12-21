from project import helper


class Driver:

    def __init__(self, name: str):
        self.name = name
        self.car = None
        self.number_of_wins: int = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        helper.value_error_if_value_contains_only_white_spaces(value, "Name should contain at least one character!")
        helper.value_error_if_value_is_empty_string(value, "Name should contain at least one character!")
        self.__name = value
