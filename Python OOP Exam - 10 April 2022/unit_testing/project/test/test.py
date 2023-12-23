from project.movie import Movie
import unittest


class Tests(unittest.TestCase):

    def test_init_creates_all_attributes(self):
        self.movie = Movie('Asd', 2000, 20)
        self.assertEqual(self.movie.name, 'Asd')
        self.assertEqual(self.movie.year, 2000)
        self.assertEqual(self.movie.rating, 20)
        self.assertEqual(self.movie.actors, [])

    def test_wrong_init_should_raise_error(self):
        with self.assertRaises(ValueError) as ve:
            Movie("", 2021, 8.5)
        self.assertEqual(str(ve.exception), "Name cannot be an empty string!")
        with self.assertRaises(ValueError) as ve:
            Movie("Dune", 120, 8.5)
        self.assertEqual(str(ve.exception), "Year is not valid!")

    def test_add_actor(self):
        a = Movie("Dune", 2021, 8.5)
        a.add_actor("Zendaya")
        a.add_actor("Rebecca Ferguson")
        self.assertEqual(a.actors, ["Zendaya", "Rebecca Ferguson"])
        result = a.add_actor("Rebecca Ferguson")
        self.assertEqual(result, "Rebecca Ferguson is already added in the list of actors!")

    def test_setter_getter_if_the_name_is_wrong(self):
        with self.assertRaises(ValueError) as ex:
            movie = Movie('', 2000, 20)
        self.assertEqual(str(ex.exception), "Name cannot be an empty string!")

    def test_setter_getter_year_if_year_is_less_than_1887(self):
        with self.assertRaises(ValueError) as ex:
            movie = Movie('Asd', 1000, 20)
        self.assertEqual(str(ex.exception), "Year is not valid!")

    def test_gt_method(self):
        a = Movie("Dune", 2021, 8.5)
        b = Movie("Titanic", 1997, 7.8)
        result = str(a > b)
        self.assertEqual(result, '"Dune" is better than "Titanic"')
        c = Movie("The Shawshank Redemption", 1994, 9.2)
        second_result = str(a > c)
        self.assertEqual(second_result, '"The Shawshank Redemption" is better than "Dune"')

    def test_greater_than_check_which_object_is_with_higher_rating(self):
        movie_1 = Movie('Asd', 2000, 20)
        movie_2 = Movie('Asd-2', 2001, 21)
        result = movie_2 > movie_1
        self.assertEqual(result, '"Asd-2" is better than "Asd"')

    def test_greater_than_check_which_object_is_with_higher_rating_part2(self):
        movie_1 = Movie('Asd', 2000, 21)
        movie_2 = Movie('Asd-2', 2001, 20)
        result = movie_2 > movie_1
        self.assertEqual(result, '"Asd" is better than "Asd-2"')

    def test_greater_than_check_which_object_is_with_higher_rating_part3(self):
        movie_1 = Movie('Asd', 2000, 21)
        movie_2 = Movie('Asd-2', 2001, 20)
        result = movie_2 > movie_1
        self.assertEqual(result, None)

    def test_the_repr_of_the_movie_object(self):
        movie = Movie('Asd', 2000, 21)
        movie.actors.append('Bozhana')
        movie.actors.append('Sonya')
        result = str(movie)
        self.assertEqual(result, f"Name: Asd\nYear of Release: 2000\nRating: 21.00\nCast: Bozhana, Sonya")

    def test_if_the_append_in_movie_actor_list_is_working(self):
        movie = Movie('Asd', 2000, 21)
        movie.actors.append('Bozhana')
        result = movie.actors
        self.assertEqual(result, ['Bozhana'])

    def test_add_actor_function_when_the_name_already_exist(self):
        movie = Movie('Asd', 2000, 21)
        movie.actors.append('Bozhana')
        result = movie.add_actor('Bozhana')
        self.assertEqual(result, f"Bozhana is already added in the list of actors!")

    def test_add_actor_function_when_the_name_is_not_exist(self):
        movie = Movie('Asd', 2000, 21)
        result = movie.add_actor('Bozhana')
        self.assertEqual(result, None)

    def test_add_actor_function_when_the_name_is_not_exist_part2(self):
        movie = Movie('Asd', 2000, 21)
        movie.add_actor('Bozhana')
        result = movie.actors
        self.assertEqual(result, ['Bozhana'])