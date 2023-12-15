from project.truck_driver import TruckDriver
import unittest


class Test(unittest.TestCase):

    def setUp(self):
        self.driver = TruckDriver('Gosho', 1)

    def test_init(self):
        self.assertEqual(self.driver.name, 'Gosho')
        self.assertEqual(self.driver.money_per_mile, 1)
        self.assertEqual(self.driver.available_cargos, {})
        self.assertEqual(self.driver.earned_money, 0.00)
        self.assertEqual(self.driver.miles, 0)

    def test_setter_getter_for_earned_money(self):
        with self.assertRaises(ValueError) as ex:
            self.driver.earned_money = -5
        self.assertEqual(str(ex.exception), f"Gosho went bankrupt.")
        self.driver.earned_money = 5
        self.assertEqual(self.driver.earned_money, 5)

    def test_add_cargo_offer(self):
        result = self.driver.add_cargo_offer('Bulgaria', 1926)
        self.assertEqual(self.driver.available_cargos, {'Bulgaria': 1926})
        self.assertEqual(result, f"Cargo for 1926 to Bulgaria was added as an offer.")

        with self.assertRaises(Exception) as ex:
            self.driver.add_cargo_offer('Bulgaria', 1926)
        self.assertEqual(str(ex.exception), "Cargo offer is already added.")

    def test_driver_best_cargo_offer_and_check_all_activities(self):
        result = self.driver.drive_best_cargo_offer()
        self.assertEqual(result, "There are no offers available.")

        self.driver.add_cargo_offer('Bulgaria', 681)
        self.driver.add_cargo_offer('Romania', 500)
        result = self.driver.drive_best_cargo_offer()
        self.assertEqual(result, f"Gosho is driving 681 to Bulgaria.")
        self.assertEqual(self.driver.miles, 681)
        self.assertEqual(self.driver.earned_money, 641)

        result1 = self.driver.drive_best_cargo_offer()
        self.assertEqual(result1, f"Gosho is driving 681 to Bulgaria.")
        self.assertEqual(self.driver.miles, 681 * 2)
        self.assertEqual(self.driver.earned_money, 641 * 2)

    def test_activity_eat(self):
        self.driver.add_cargo_offer('Bulgaria', 250)
        self.driver.drive_best_cargo_offer()
        self.assertEqual(self.driver.earned_money, 230)
        self.assertEqual(self.driver.miles, 250)

    def test_activity_sleep(self):
        self.driver.add_cargo_offer('Bulgaria', 1000)
        self.driver.drive_best_cargo_offer()
        self.assertEqual(self.driver.earned_money, 875)

    def test_activity_pump_gas(self):
        self.driver.add_cargo_offer('Bulgaria', 1500)
        self.driver.drive_best_cargo_offer()
        result = 20 * 6 + 45 + 500
        self.assertEqual(self.driver.earned_money, 1500 - result)

    def test_activity_repair_truck(self):
        self.driver.money_per_mile = 20
        self.driver.add_cargo_offer('Bulgaria', 10000)
        self.driver.drive_best_cargo_offer()
        result = (10000 // 250) * 20 + (10000 // 1000) * 45 + (10000 // 1500) * 500 + 7500
        self.assertEqual(self.driver.earned_money, 10000 * 20 - result)

    def test_bankrupt(self):
        with self.assertRaises(ValueError) as ex:
            self.driver.add_cargo_offer('Bulgaria', 10000)
            self.driver.drive_best_cargo_offer()
        self.assertEqual(str(ex.exception), 'Gosho went bankrupt.')

    def test_repr(self):
        self.driver.miles = 5
        self.assertEqual(str(self.driver), f"Gosho has 5 miles behind his back.")

