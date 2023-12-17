from project.movie_specification.movie import Movie
from project.user import User
from project.movie_specification.fantasy import Fantasy
from project.movie_specification.action import Action


class MovieApp:

    def __init__(self):
        self.movies_collection: list = []
        self.users_collection: list = []

    def __find_user(self, username):
        for user in self.users_collection:
            if user.username == username:
                return user

    def register_user(self, username: str, age: int):
        if self.__find_user(username) is not None:
            raise Exception(f"User already exists!")

        new_user = User(username, age)
        self.users_collection.append(new_user)
        return f"{username} registered successfully."

    def upload_movie(self, username: str, movie: Movie):
        user = self.__find_user(username)
        if user is None:
            raise Exception(f"This user does not exist!")

        if user.username != movie.owner.username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        if movie in self.movies_collection:
            raise Exception(f"Movie already added to the collection!")

        user.movies_owned.append(movie)
        self.movies_collection.append(movie)
        return f"{username} successfully added {movie.title} movie."

    def edit_movie(self, username: str, movie: Movie, **kwargs):
        user = self.__find_user(username)

        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        if user.username != movie.owner.username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        for movie_attribute, new_value in kwargs.items():
            if movie_attribute == 'title':
                movie.title = new_value
            elif movie_attribute == 'year':
                movie.year = new_value
            elif movie_attribute == 'age_restriction':
                movie.age_restriction = new_value

        return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self, username: str, movie: Movie):
        user = self.__find_user(username)

        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        if movie.owner.username != user.username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        user.movies_owned.remove(movie)
        self.movies_collection.remove(movie)

        return f"{username} successfully deleted {movie.title} movie."

    def like_movie(self, username: str, movie: Movie):
        user = self.__find_user(username)

        if user.username == movie.owner.username:
            raise Exception(f"{username} is the owner of the movie {movie.title}!")

        if movie in user.movies_liked:
            raise Exception(f"{username} already liked the movie {movie.title}!")

        movie.likes += 1
        user.movies_liked.append(movie)
        return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username: str, movie: Movie):
        user = self.__find_user(username)

        if movie not in user.movies_liked:
            raise Exception(f"{username} has not liked the movie {movie.title}!")

        movie.likes -= 1
        user.movies_liked.remove(movie)

        return f"{username} disliked {movie.title} movie."

    def display_movies(self):
        result = []
        if not self.movies_collection:
            result.append("No movies found.")
        else:
            sorted_movies_list = list(sorted(self.movies_collection, key=lambda movie: (-movie.year, movie.title)))
            for movie in sorted_movies_list:
                result.append(movie.details())

        return '\n'.join(result)

    def __str__(self):
        users_info = f"All users: {', '.join([user.username for user in self.users_collection]) if self.users_collection else 'No users.'}"
        movies_info = f"All movies: {', '.join([movie.title for movie in self.movies_collection]) if self.movies_collection else 'No movies.'}"
        return users_info + '\n' + movies_info


movie_app = MovieApp()
print(movie_app.register_user('Martin', 24))
user = movie_app.users_collection[0]
movie = Action('Die Hard', 1988, user, 18)
print(movie_app.upload_movie('Martin', movie))
print(movie_app.movies_collection[0].title)
print(movie_app.register_user('Alexandra', 25))
user2 = movie_app.users_collection[1]
movie2 = Action('Free Guy', 2021, user2, 16)
print(movie_app.upload_movie('Alexandra', movie2))
print(movie_app.edit_movie('Alexandra', movie2, title="Free Guy 2"))
print(movie_app.like_movie('Martin', movie2))
print(movie_app.like_movie('Alexandra', movie))
print(movie_app.dislike_movie('Martin', movie2))
print(movie_app.like_movie('Martin', movie2))
print(movie_app.delete_movie('Alexandra', movie2))
movie2 = Fantasy('The Lord of the Rings', 2003, user2, 14)
print(movie_app.upload_movie('Alexandra', movie2))
print(movie_app.display_movies())
print(movie_app)
