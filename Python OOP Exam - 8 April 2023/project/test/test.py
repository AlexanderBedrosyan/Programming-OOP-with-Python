from project.tennis_player import TennisPlayer
import unittest


class Test(unittest.TestCase):

    def setUp(self):
        self.tennis_player = TennisPlayer('Gosho', 19, 25)

    def test___init__(self):
        self.assertEqual(self.tennis_player.name, 'Gosho')
        self.assertEqual(self.tennis_player.age, 19)
        self.assertEqual(self.tennis_player.points, 25)
        self.assertEqual(self.tennis_player.wins, [])
        self.assertEqual(len(self.tennis_player.wins), 0)

    def test__name_setter(self):
        with self.assertRaises(ValueError) as ve:
            self.tennis_player.name = 'Gs'
        self.assertEqual(str(ve.exception), "Name should be more than 2 symbols!")

        with self.assertRaises(ValueError) as ve:
            self.tennis_player.name = ''
        self.assertEqual(str(ve.exception), "Name should be more than 2 symbols!")

    def test__age_setter(self):
        with self.assertRaises(ValueError) as ve:
            self.tennis_player.age = 17
        self.assertEqual(str(ve.exception), "Players must be at least 18 years of age!")

    def test__add_new_win(self):
        self.tennis_player.add_new_win('Sofia open')
        self.tennis_player.add_new_win('Burgas open')
        self.assertEqual(self.tennis_player.wins, ['Sofia open', 'Burgas open'])
        self.assertEqual(len(self.tennis_player.wins), 2)

        result = self.tennis_player.add_new_win('Sofia open')
        self.assertEqual(result, f"Sofia open has been already added to the list of wins!")

    def test___lt__(self):
        player2 = TennisPlayer('Doncho', 22, 11)
        result = self.tennis_player < player2
        self.assertEqual(result, f'{self.tennis_player.name} is a better player than {player2.name}')

        self.assertEqual(self.tennis_player == player2, False)

        result2 = self.tennis_player > player2
        self.assertEqual(result2, f'{self.tennis_player.name} is a top seeded player and he/she is better than {player2.name}')

        player2.points = 55

        result3 = player2 < self.tennis_player
        self.assertEqual(result3, f'{player2.name} is a better player than {self.tennis_player.name}')

        self.assertEqual(self.tennis_player == player2, False)

        result4 = player2 > self.tennis_player
        self.assertEqual(result4,f'{player2.name} is a top seeded player and he/she is better than {self.tennis_player.name}')

        self.tennis_player.points = 55

        result5 = player2 > self.tennis_player
        self.assertEqual(result5,
                         f'{self.tennis_player.name} is a better player than {player2.name}')

    def test___str__(self):
        result1 = f"Tennis Player: {self.tennis_player.name}\n" \
               f"Age: {self.tennis_player.age}\n" \
               f"Points: {self.tennis_player.points:.1f}\n" \
               f"Tournaments won: {', '.join(self.tennis_player.wins)}"
        self.assertEqual(str(self.tennis_player), result1)

        self.tennis_player.add_new_win('Sofia open')
        self.tennis_player.add_new_win('Burgas open')
        result = f"Tennis Player: {self.tennis_player.name}\n" \
               f"Age: {self.tennis_player.age}\n" \
               f"Points: {self.tennis_player.points:.1f}\n" \
               f"Tournaments won: {', '.join(self.tennis_player.wins)}"
        self.assertEqual(str(self.tennis_player), result)
