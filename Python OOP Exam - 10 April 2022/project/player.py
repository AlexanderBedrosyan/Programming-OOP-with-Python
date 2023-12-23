from project import helper


class Player:
    CREATED_PLAYERS = []

    def __init__(self, name: str, age: int, stamina=100):
        self.name = name
        self.age = age
        self.stamina = stamina

    @property
    def need_sustenance(self):
        return self.stamina < 100

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Name not valid!")
        helper.value_error_if_value_is_empty_string(value, "Name not valid!")
        if value in Player.CREATED_PLAYERS:
            raise Exception(f"Name {value} is already used!")
        Player.CREATED_PLAYERS.append(value)
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        helper.value_error_if_number_is_less_than_other_number(value, 12, "The player cannot be under 12 years old!")
        self.__age = value

    @property
    def stamina(self):
        return self.__stamina

    @stamina.setter
    def stamina(self, value):
        helper.value_error_if_value_is_negative_number(value, "Stamina not valid!")
        helper.value_error_if_number_is_bigger_than_other_number(value, 100, "Stamina not valid!")
        self.__stamina = value

    def __str__(self):
        return f"Player: {self.name}, {self.age}, {self.stamina}, {self.need_sustenance}"
