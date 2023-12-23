from project.robot import Robot
import unittest


class RobotTest(unittest.TestCase):

    def setUp(self):
        self.robot = Robot("Alex", "Education", 5, 22.5)

    def test__robot_id(self):
        result = "Alex"
        self.assertEqual(self.robot.robot_id, result)

    def test__category(self):
        result = "Education"
        self.assertEqual(self.robot.category, result)

    def test__capacity(self):
        result = 5
        self.assertEqual(self.robot.available_capacity, result)

    def test__price(self):
        result = 22.5
        self.assertEqual(self.robot.price, result)

    def test__capacity_property(self):
        with self.assertRaises(ValueError) as example:
            self.robot.category = "Mitko"
        result = example.exception
        expect = f"Category should be one of '{self.robot.ALLOWED_CATEGORIES}'"
        self.assertEqual(str(result), expect)

    def test__price_property(self):
        with self.assertRaises(ValueError) as example:
            self.robot.price = -1
        result = example.exception
        expect = f"Price cannot be negative!"
        self.assertEqual(str(result), expect)

    def test__upgrade_successfully(self):
        result = self.robot.upgrade("hand", 12.3)
        expect = "Robot Alex was upgraded with hand."
        self.assertEqual(result, expect)

        result = self.robot.upgrade("head", 12.8)
        expect = "Robot Alex was upgraded with head."
        self.assertEqual(result, expect)

    def test__upgrade_unsuccessfully(self):
        self.robot.hardware_upgrades = ["hand"]
        result = self.robot.upgrade("hand", 12.3)
        expect = "Robot Alex was not upgraded."
        self.assertEqual(result, expect)

    def test__update_successfully_software(self):
        result = self.robot.update(2, 3)
        expect = "Robot Alex was updated to version 2."
        self.assertEqual(result, expect)

    def test__update_unsuccessfully_software(self):
        self.robot.software_updates = [1, 2, 6]
        result = self.robot.update(2, 3)
        expect = "Robot Alex was not updated."
        self.assertEqual(result, expect)

    def test__update_unsuccessfully_software_part2(self):
        self.robot.available_capacity = 8
        result = self.robot.update(2, 15)
        expect = "Robot Alex was not updated."
        self.assertEqual(result, expect)

    def test__if_price_higher_than_other_price_func_gt(self):
        robot_2 = Robot("1", "Military", 10, 0)

        self.robot.price = 2

        result = self.robot > robot_2
        expect = "Robot with ID Alex is more expensive than Robot with ID 1."
        self.assertEqual(result, expect)

    def test__if_price_equal_than_other_price_func_gt(self):
        robot_2 = Robot("1", "Military", 10, 1)

        self.robot.price = 1

        result = self.robot > robot_2
        expect = "Robot with ID Alex costs equal to Robot with ID 1."
        self.assertEqual(result, expect)

    def test__if_price_smaller_than_other_price_func_gt(self):
        robot_2 = Robot("1", "Military", 10, 1)

        self.robot.price = 0

        result = self.robot > robot_2
        expect = "Robot with ID Alex is cheaper than Robot with ID 1."
        self.assertEqual(result, expect)


if __name__ == '__main__':
    unittest.main()
