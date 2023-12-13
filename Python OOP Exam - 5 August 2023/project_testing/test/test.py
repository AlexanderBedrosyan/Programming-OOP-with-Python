from project.second_hand_car import SecondHandCar
import unittest


class Test(unittest.TestCase):

    def setUp(self):
        self.car = SecondHandCar('Opel', 'Vecta', 120, 1500.00)

    def test___init__(self):
        self.assertEqual(self.car.model, 'Opel')
        self.assertEqual(self.car.car_type, 'Vecta')
        self.assertEqual(self.car.mileage, 120)
        self.assertEqual(self.car.price, 1500.00)
        self.assertEqual(self.car.repairs, [])
        self.assertEqual(len(self.car.repairs), 0)

    def test_price_setter(self):
        with self.assertRaises(ValueError) as ve:
            self.car.price = 1.0
        self.assertEqual(str(ve.exception), 'Price should be greater than 1.0!')

        with self.assertRaises(ValueError) as ve:
            self.car.price = 0.9
        self.assertEqual(str(ve.exception), 'Price should be greater than 1.0!')

        with self.assertRaises(ValueError) as ve:
            self.car.mileage = 100
        self.assertEqual(str(ve.exception), 'Please, second-hand cars only! Mileage must be greater than 100!')

        with self.assertRaises(ValueError) as ve:
            self.car.mileage = 1
        self.assertEqual(str(ve.exception), 'Please, second-hand cars only! Mileage must be greater than 100!')

    def test_set_promotional_price(self):
        with self.assertRaises(ValueError) as ve:
            self.car.set_promotional_price(1500.00)
        self.assertEqual(str(ve.exception), 'You are supposed to decrease the price!')

        with self.assertRaises(ValueError) as ve:
            self.car.set_promotional_price(1600.00)
        self.assertEqual(str(ve.exception), 'You are supposed to decrease the price!')

        result = self.car.set_promotional_price(1499.00)
        self.assertEqual(result, 'The promotional price has been successfully set.')
        self.assertEqual(self.car.price, 1499.00)

    def test_need_repair(self):
        result = self.car.need_repair(751, 'Neshto se e preebalo')
        self.assertEqual(result, 'Repair is impossible!')

        result2 = self.car.need_repair(20, 'Oil change')
        self.assertEqual(result2, f'Price has been increased due to repair charges.')
        self.assertEqual(self.car.price, 1520.00)
        self.assertEqual(self.car.repairs, ['Oil change'])
        self.assertEqual(len(self.car.repairs), 1)

        result2 = self.car.need_repair(80, 'Broken window')
        self.assertEqual(result2, f'Price has been increased due to repair charges.')
        self.assertEqual(self.car.price, 1600.00)
        self.assertEqual(self.car.repairs, ['Oil change', 'Broken window'])
        self.assertEqual(len(self.car.repairs), 2)

    def test___gt__(self):
        new_car = SecondHandCar('Opel', 'Astra', 1000, 2000)
        result = self.car > new_car
        self.assertEqual(result, 'Cars cannot be compared. Type mismatch!')

        final_car = SecondHandCar('Opel', 'Vecta', 120, 2000.20)
        result2 = self.car > final_car
        self.assertEqual(result2, False)

        final_car2 = SecondHandCar('Opel', 'Vecta', 120, 1500.00)
        result3 = self.car > final_car2
        self.assertEqual(result3, False)

        final_car = SecondHandCar('Opel', 'Vecta', 120, 1000.00)
        result4 = self.car > final_car
        self.assertEqual(result4, True)

        final_car = SecondHandCar('Mazda', 'Vecta', 120, 2000.20)
        result5 = self.car > final_car
        self.assertEqual(result5, False)

    def test___str__(self):
        self.car.need_repair(20, 'Oil change')
        result = str(self.car)
        needed_result = f"Model Opel | Type Vecta | Milage 120km\nCurrent price: 1520.00 | Number of Repairs: 1"
        self.assertEqual(result, needed_result)

        self.car.need_repair(80, 'Windows broken')
        result2 = str(self.car)
        needed_result2 = f"Model Opel | Type Vecta | Milage 120km\nCurrent price: 1600.00 | Number of Repairs: 2"
        self.assertEqual(result2, needed_result2)
