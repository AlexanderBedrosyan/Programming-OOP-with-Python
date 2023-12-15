from project import helper


class Band:

    def __init__(self, name: str):
        self.name = name
        self.members = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        message = "Band name should contain at least one character!"
        helper.value_error_if_value_is_empty_string(value, message)
        self.__name = value

    def __str__(self):
        return f"{self.name} with {len(self.members)} members."
