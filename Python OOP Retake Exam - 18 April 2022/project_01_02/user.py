from project import helper


class User:

    def __init__(self, username: str, age: int):
        self.username = username
        self.age = age
        self.movies_liked: list = []
        self.movies_owned: list = []

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        message = "Invalid username!"
        helper.value_error_if_value_is_empty_string(value, message)
        self.__username = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        message = f"Users under the age of 6 are not allowed!"
        helper.value_error_if_number_is_less_than_other_number(value, 6, message)
        self.__age = value

    def __str__(self):
        result = [
            f"Username: {self.username}, Age: {self.age}",
            f"Liked movies:"
        ]
        if not self.movies_liked:
            result.append("No movies liked.")
        else:
            for movie in self.movies_liked:
                result.append(movie.details())
        result.append("Owned movies:")
        if not self.movies_owned:
            result.append("No movies owned.")
        else:
            for movie in self.movies_owned:
                result.append(movie.details())
        return '\n'.join(result)