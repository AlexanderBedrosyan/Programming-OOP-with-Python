from project import helper
from project.movie_specification.movie import Movie


class Thriller(Movie):

    def __init__(self, title, year, owner, age_restriction=16):
        super().__init__(title, year, owner, age_restriction)

    @property
    def age_restriction(self):
        return self.__age_restriction

    @age_restriction.setter
    def age_restriction(self, value):
        message = "Thriller movies must be restricted for audience under 16 years!"
        helper.value_error_if_number_is_less_than_other_number(value, 16, message)
        self.__age_restriction = value

    def details(self):
        return f"Thriller - Title:{self.title}, Year:{self.year}, Age restriction:{self.age_restriction}, Likes:{self.likes}, Owned by:{self.owner.username}"