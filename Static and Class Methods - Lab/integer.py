from math import floor


class Integer:

    def __init__(self, value: int):
        self.value = value

    @staticmethod
    def roman_to_arabic(roman):
        roman_numerals = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        arabic = 0
        prev_value = 0

        for numeral in reversed(roman):
            value = roman_numerals[numeral]
            if value < prev_value:
                arabic -= value
            else:
                arabic += value
            prev_value = value

        return arabic

    @classmethod
    def from_float(cls, float_value):
        if type(float_value) != float:
            return 'value is not a float'
        return cls(floor(float_value))

    @classmethod
    def from_roman(cls, value):
        new_value = Integer.roman_to_arabic(value)
        return cls(new_value)

    @classmethod
    def from_string(cls, value):
        if type(value) == str:
            try:
                return cls(int(value))
            except IndexError:
                return "wrong type"
        return "wrong type"


# class IntegerTests(unittest.TestCase):
#     def test_basic_init(self):
#         integer = Integer(1)
#         self.assertEqual(integer.value, 1)
#
#     def test_from_float_success(self):
#         integer = Integer.from_float(2.5)
#         self.assertEqual(integer.value, 2)
#
#     def test_from_float_wrong_type(self):
#         result = Integer.from_float("2.5")
#         self.assertEqual(result, "value is not a float")
#
#     def test_from_roman(self):
#         integer = Integer.from_roman("XIX")
#         self.assertEqual(integer.value, 19)
#
#     def test_from_string_success(self):
Integer = Integer(1)
print(Integer.from_string("10"))
#         self.assertEqual(integer.value, 10)
#
#     def test_from_string_wrong_type(self):
#         result = Integer.from_string(1.5)
#         self.assertEqual(result, "wrong type")
#
#
# if __name__ == "__main__":
#     unittest.main()