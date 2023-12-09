from unittest import TestCase, main


class TestCar(TestCase):

    def setUp(self):
        self.car = Car("Opel", "Corsa", 10, 80)

    def test_successful_initialization(self):
        self.assertEqual("Opel", self.car.make)
        self.assertEqual("Corsa", self.car.model)
        self.assertEqual(10, self.car.fuel_consumption)
        self.assertEqual(80, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_empty_make(self):
        expected = "Make cannot be null or empty!"
        with self.assertRaises(Exception) as ex:
            Car("", "Corsa", 10, 80)
        self.assertEqual(expected, str(ex.exception))

    def test_empty_model(self):
        expected = "Model cannot be null or empty!"
        with self.assertRaises(Exception) as ex:
            Car("Opel", "", 10, 80)
        self.assertEqual(expected, str(ex.exception))

    def test_fuel_consumption_lower_or_equal_to_0_check_error(self):
        expected = "Fuel consumption cannot be zero or negative!"
        with self.assertRaises(Exception) as ex:
            Car("Opel", "Corsa", 0, 80)
        self.assertEqual(expected, str(ex.exception))

    def test_fuel_capacity_cannot_be_lower_or_equal_to_0(self):
        expected = "Fuel capacity cannot be zero or negative!"
        with self.assertRaises(Exception) as ex:
            Car("Opel", "Corsa", 10, 0)
        self.assertEqual(expected, str(ex.exception))

    def test_fuel_amount_cannot_be_lower_than_zero(self):
        expected = "Fuel amount cannot be negative!"
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -1
        self.assertEqual(expected, str(ex.exception))

    def test_refuel_method_cannot_be_zero_or_lower(self):
        expected = "Fuel amount cannot be zero or negative!"
        with self.assertRaises(Exception) as ex:
            self.car.refuel(0)
        self.assertEqual(expected, str(ex.exception))

    def test_fuel_amount_go_up_after_refuel(self):
        expected = 10
        self.car.refuel(10)
        self.assertEqual(expected, self.car.fuel_amount)

    def test_fuel_amount_set_back_to_max_capacity(self):
        expected = 80
        self.car.refuel(200)
        self.assertEqual(expected, self.car.fuel_amount)

    def test_if_the_fuel_is_enough_to_drive(self):
        expected = "You don't have enough fuel to drive!"
        with self.assertRaises(Exception) as ex:
            self.car.drive(2000)
        self.assertEqual(expected, str(ex.exception))

    def test_if_fuel_amount_is_lowered_after_driving(self):
        expected = 20
        self.car.fuel_amount = 40
        self.car.drive(200)
        self.assertEqual(expected, self.car.fuel_amount)


if __name__ == "__main__":
    main()