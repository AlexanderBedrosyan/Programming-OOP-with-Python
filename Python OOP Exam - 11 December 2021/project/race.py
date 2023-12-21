from project import helper


class Race:

    def __init__(self, name: str):
        self.name = name
        self.drivers: list = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        helper.value_error_if_value_is_empty_string(value, "Name cannot be an empty string!")
        self.__name = value