from project import helper
from project.movie_specification.movie import Movie


class Action(Movie):

    def __init__(self, title, year, owner, age_restriction=12):
        super().__init__(title, year, owner, age_restriction)

    @property
    def age_restriction(self):
        return self.__age_restriction

    @age_restriction.setter
    def age_restriction(self, value):
        message = "Action movies must be restricted for audience under 12 years!"
        helper.value_error_if_number_is_less_than_other_number(value, 12, message)
        self.__age_restriction = value

    def details(self):
        return f"Action - Title:{self.title}, Year:{self.year}, Age restriction:{self.age_restriction}, Likes:{self.likes}, Owned by:{self.owner.username}"