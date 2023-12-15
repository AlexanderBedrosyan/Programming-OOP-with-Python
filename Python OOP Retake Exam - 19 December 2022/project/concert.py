from project import helper


class Concert:

    def __init__(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        self.genre = genre
        self.audience = audience
        self.ticket_price = ticket_price
        self.expenses = expenses
        self.place = place

    @property
    def genre(self):
        return self.__genre

    @genre.setter
    def genre(self, value):
        if value not in ["Metal", "Rock", "Jazz"]:
            raise ValueError(f"Our group doesn't play {value}!")
        self.__genre = value

    @property
    def audience(self):
        return self.__audience

    @audience.setter
    def audience(self, value):
        message = "At least one person should attend the concert!"
        helper.value_error_if_number_is_less_than_other_number(value, 1, message)
        self.__audience = value

    @property
    def ticket_price(self):
        return self.__ticket_price

    @ticket_price.setter
    def ticket_price(self, value):
        message = "Ticket price must be at least 1.00$!"
        helper.value_error_if_number_is_less_than_other_number(value, 1.00, message)
        self.__ticket_price = value

    @property
    def expenses(self):
        return self.__expenses

    @expenses.setter
    def expenses(self, value):
        message = "Expenses cannot be a negative number!"
        helper.value_error_if_number_is_less_than_other_number(value, 0.00, message)
        self.__expenses = value

    @property
    def place(self):
        return self.__place

    @place.setter
    def place(self, value):
        message = "Place must contain at least 2 chars. It cannot be empty!"
        helper.value_error_if_number_is_less_than_other_number(len(value), 2, message)
        helper.value_error_if_value_contains_only_white_spaces(value, message)
        self.__place = value

    def __str__(self):
        return f"{self.genre} concert at {self.place}."
