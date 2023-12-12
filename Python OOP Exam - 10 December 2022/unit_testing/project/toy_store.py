class ToyStore:
    def __init__(self):
        self.toy_shelf = {
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }

    def add_toy(self, shelf: str, toy_name: str):
        if shelf not in self.toy_shelf.keys():
            raise Exception("Shelf doesn't exist!")
        if self.toy_shelf[shelf] == toy_name:
            raise Exception("Toy is already in shelf!")
        if self.toy_shelf[shelf] is not None:
            raise Exception("Shelf is already taken!")
        self.toy_shelf[shelf] = toy_name
        return f"Toy:{toy_name} placed successfully!"

    def remove_toy(self, shelf: str, toy_name: str):
        if shelf not in self.toy_shelf.keys():
            raise Exception("Shelf doesn't exist!")
        if self.toy_shelf[shelf] != toy_name:
            raise Exception("Toy in that shelf doesn't exists!")
        self.toy_shelf[shelf] = None
        return f"Remove toy:{toy_name} successfully!"


import unittest


class Tests(unittest.TestCase):

    def setUp(self):
        self.toy_store = ToyStore()

    def test_init_creates_all_attributes(self):
        self.assertEqual(self.toy_store.toy_shelf['A'], None)
        self.assertEqual(self.toy_store.toy_shelf['B'], None)
        self.assertEqual(self.toy_store.toy_shelf['C'], None)
        self.assertEqual(self.toy_store.toy_shelf['D'], None)
        self.assertEqual(self.toy_store.toy_shelf['E'], None)
        self.assertEqual(self.toy_store.toy_shelf['F'], None)
        self.assertEqual(self.toy_store.toy_shelf['G'], None)

    def test_add_toy_is_shelf_not_in_toy_store(self):
        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy('K', 'ToyTestName')
        self.assertEqual(str(ex.exception), "Shelf doesn't exist!")

    def test_add_toy_is_toy_already_in_the_shelf(self):
        self.toy_store.add_toy('A', 'ToyTestName')
        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy('A', 'ToyTestName')
        self.assertEqual(str(ex.exception), "Toy is already in shelf!")

    def test_add_toy_is_shelf_already_taken(self):
        self.toy_store.add_toy('A', 'ToyTestName')
        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy('A', 'ToyTestName2')
        self.assertEqual(str(ex.exception), "Shelf is already taken!")

    def test_add_toy_successfully_on_the_shelf(self):
        result = self.toy_store.add_toy('A', 'ToyTestName')

        self.assertEqual(result, "Toy:ToyTestName placed successfully!")

        self.assertEqual(self.toy_store.toy_shelf, {
            "A": "ToyTestName",
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        })

    def test_remove_toy_is_shelf_in_toy_store(self):
        with self.assertRaises(Exception) as ex:
            self.toy_store.remove_toy('wrong_shelf', 'ToyTestName')
        self.assertEqual(str(ex.exception), "Shelf doesn't exist!")

    def test_remove_toy_is_toy_name_exist_on_the_exact_shelf(self):
        with self.assertRaises(Exception) as ex:
            self.toy_store.remove_toy('A', 'ToyTestName2')
        self.assertEqual(str(ex.exception), "Toy in that shelf doesn't exists!")

    def test_remove_toy_successfully_removed_toy_from_shelf(self):
        self.toy_store.add_toy('A', 'ToyTestName')
        result = self.toy_store.remove_toy('A', 'ToyTestName')

        self.assertEqual(result, "Remove toy:ToyTestName successfully!")
        self.assertEqual(self.toy_store.toy_shelf, {
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        })
