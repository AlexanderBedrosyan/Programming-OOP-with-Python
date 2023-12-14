from project.pet_shop import PetShop
import unittest


class Tests(unittest.TestCase):

    def setUp(self):
        self.pet_shop = PetShop("Bo")

    def test_check_init_if_everything_is_correct(self):
        self.assertEqual(self.pet_shop.name, 'Bo')
        self.assertEqual(self.pet_shop.food, {})
        self.assertEqual(self.pet_shop.pets, [])

    def test_value_error_add_food(self):
        with self.assertRaises(ValueError) as ex:
            self.pet_shop.add_food('hhh', -1)
        self.assertEqual(str(ex.exception), 'Quantity cannot be equal to or less than 0')
        with self.assertRaises(ValueError) as ex:
            self.pet_shop.add_food('hhh', 0)
        self.assertEqual(str(ex.exception), 'Quantity cannot be equal to or less than 0')

    def test_add_food_successfully(self):
        result = self.pet_shop.add_food('gosho', 5)
        self.assertEqual(result, 'Successfully added 5.00 grams of gosho.')
        self.assertEqual(self.pet_shop.food, {'gosho': 5.00})
        self.pet_shop.add_food('gosho', 10)
        self.assertEqual(self.pet_shop.food, {'gosho': 15.00})

    def test_exception_and_success_add_pet(self):
        result = self.pet_shop.add_pet('gosho')
        self.assertEqual(result, f"Successfully added gosho.")
        self.assertEqual(self.pet_shop.pets, ['gosho'])
        with self.assertRaises(Exception) as ex:
            self.pet_shop.add_pet('gosho')
        self.assertEqual(str(ex.exception), "Cannot add a pet with the same name")

    def test_feed_pet(self):
        self.pet_shop.add_pet('gosho')
        self.pet_shop.add_food('hlyab', 1000)
        result = self.pet_shop.feed_pet('hlyab', 'gosho')
        self.assertEqual(result, f"gosho was successfully fed")
        self.assertEqual(self.pet_shop.food, {'hlyab': 900})
        with self.assertRaises(Exception) as ex:
            self.pet_shop.feed_pet('hlyab','traycho')
        self.assertEqual(str(ex.exception), "Please insert a valid pet name")
        result1 = self.pet_shop.feed_pet('mlyako','gosho')
        self.assertEqual(result1, 'You do not have mlyako')
        self.pet_shop.add_food('mlyako', 10)
        result = self.pet_shop.feed_pet('mlyako', 'gosho')
        self.assertEqual(result, "Adding food...")
        self.assertEqual(self.pet_shop.food, {'hlyab': 900, 'mlyako': 1010.00})

    def test_repr(self):
        result1 = f'Shop {self.pet_shop.name}:\n' \
               f'Pets: '
        self.assertEqual(str(self.pet_shop), result1)
        self.pet_shop.add_pet('gosho')
        self.pet_shop.add_pet('tosho')
        result = f'Shop {self.pet_shop.name}:\n' \
               f'Pets: {", ".join(self.pet_shop.pets)}'
        self.assertEqual(str(self.pet_shop), result)
