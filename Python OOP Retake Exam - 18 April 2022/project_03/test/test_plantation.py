from project.plantation import Plantation
import unittest


class Test(unittest.TestCase):

    def setUp(self):
        self.plantation = Plantation(5)

    def test_init(self):
        self.assertEqual(self.plantation.size, 5)
        self.assertEqual(self.plantation.plants, {})
        self.assertEqual(self.plantation.workers, [])

    def test_size_setter(self):
        with self.assertRaises(ValueError) as ve:
            Plantation(-1)
        self.assertEqual(str(ve.exception), "Size must be positive number!")

        new_plantation = Plantation(0)
        self.assertEqual(new_plantation.size, 0)

    def test_hire_worker(self):
        result = self.plantation.hire_worker('Bozhana')
        self.assertEqual(result, "Bozhana successfully hired.")

        with self.assertRaises(ValueError) as ve:
            self.plantation.hire_worker('Bozhana')
        self.assertEqual(str(ve.exception), 'Worker already hired!')

    def test___len__(self):
        self.plantation.plants = {'flowers': [1, 2, 3, 4], 'flowers2': [2, 3]}
        self.assertEqual(len(self.plantation), 6)

        self.plantation.plants = {}
        self.assertEqual(len(self.plantation), 0)

    def test_planting(self):
        self.plantation.workers = ['Bozhana', 'Peter', 'Margarit']

        with self.assertRaises(ValueError) as ve:
            self.plantation.planting('Grigorii', 'flower')
        self.assertEqual(str(ve.exception), f"Worker with name Grigorii is not hired!")

        with self.assertRaises(ValueError) as ve:
            self.plantation.plants = {'Flowers': [1, 2, 3, 4, 5, 6, 7]}
            self.plantation.planting('Bozhana', 'flower')
        self.assertEqual(str(ve.exception), "The plantation is full!")

        self.plantation.plants = {'Margarit': ['1', '2']}
        self.plantation.planting('Bozhana', '1')
        self.assertEqual(self.plantation.plants, {'Margarit': ['1', '2'], 'Bozhana': ['1']})

        self.plantation.planting('Margarit', '5')
        self.assertEqual(self.plantation.plants, {'Margarit': ['1', '2', '5'], 'Bozhana': ['1']})

        self.plantation.planting('Peter', '12')
        self.assertEqual(self.plantation.plants, {'Margarit': ['1', '2', '5'], 'Bozhana': ['1'], 'Peter': ['12']})

        with self.assertRaises(ValueError) as ve:
            self.plantation.planting('Peter', 'flower')
        self.assertEqual(str(ve.exception), "The plantation is full!")

        new_plantation = Plantation(5)
        new_plantation.workers = ['Mitka', 'Kitka']

        result1926 = new_plantation.planting('Kitka', '1')
        self.assertEqual(result1926, "Kitka planted it's first 1.")
        self.assertEqual(new_plantation.plants, {'Kitka': ['1']})

        self.assertEqual(new_plantation.planting('Kitka', '2'), 'Kitka planted 2.')

        final_plantation = Plantation(0)
        final_plantation.workers = ['Bozhi', "Sasho"]

        with self.assertRaises(ValueError) as ve:
            final_plantation.planting('Bozhi', '2')
        self.assertEqual(str(ve.exception), "The plantation is full!")

    def test___str__(self):
        self.plantation.workers = ['Bozhana', 'Peter', 'Margarit']
        self.plantation.plants = {'Margarit': ['1', '2', '5'], 'Bozhana': ['1'], 'Peter': ['12']}
        result = str(self.plantation)

        needed_result = [
            "Plantation size: 5",
            "Bozhana, Peter, Margarit",
            "Margarit planted: 1, 2, 5",
            "Bozhana planted: 1",
            "Peter planted: 12"
        ]

        self.assertEqual(result, '\n'.join(needed_result))

        self.plantation.workers = []
        self.plantation.plants = {}
        result2 = str(self.plantation)
        self.assertEqual(result2, "Plantation size: 5\n")

        self.plantation.workers = ['Bozhana', 'Peter', 'Margarit']
        result3 = str(self.plantation)
        self.assertEqual(result3, "Plantation size: 5\nBozhana, Peter, Margarit",)

        self.plantation.plants = {'Bozhana': []}
        result4 = str(self.plantation)
        self.assertEqual(result4, "Plantation size: 5\nBozhana, Peter, Margarit\nBozhana planted: ")

    def test___repr__(self):
        self.plantation.workers = ['Bozhana', 'Peter', 'Margarit']

        result = self.plantation.__repr__()
        self.assertEqual(result, 'Size: 5\nWorkers: Bozhana, Peter, Margarit')

        self.plantation.workers = []
        result2 = self.plantation.__repr__()
        self.assertEqual(result2, 'Size: 5\nWorkers: ')

    def test_successfully_hire_worker(self):
        self.assertEqual("Tamer successfully hired.", self.plantation.hire_worker("Tamer"))
        self.assertEqual(["Tamer"], self.plantation.workers)
        self.assertEqual(1, len(self.plantation.workers))

        self.plantation.hire_worker("Tamer_2")
        self.assertEqual(["Tamer", "Tamer_2"], self.plantation.workers)
        self.assertEqual(2, len(self.plantation.workers))

