from project.trip import Trip
import unittest


class Tests(unittest.TestCase):

    def setUp(self):
        self.current_trip = Trip(4000, 3, False)

    def test_init_creates_all_attributes(self):
        self.assertEqual(self.current_trip.budget, 4000)
        self.assertEqual(self.current_trip.travelers, 3)
        self.assertEqual(self.current_trip.is_family, False)
        self.assertEqual(self.current_trip.DESTINATION_PRICES_PER_PERSON, {'New Zealand': 7500, 'Australia': 5700, 'Brazil': 6200, 'Bulgaria': 500})

    def test_if_travelers_getter_setter_raise_value_error(self):
        with self.assertRaises(ValueError) as ex:
            result = Trip(20, 0, False)
        self.assertEqual(str(ex.exception), 'At least one traveler is required!')

    def test_if_is_family_getter_setter_return_the_correct_result(self):
        trip_for_false = Trip(20, 1, True)
        self.assertEqual(trip_for_false.is_family, False)
        trip_for_true_part_1 = Trip(20, 3, True)
        self.assertEqual(trip_for_true_part_1.is_family, True)
        trip_for_false_part2 = Trip(20, 3, False)
        self.assertEqual(trip_for_false_part2.is_family, False)
        trip_for_false_part3 = Trip(20, 1, False)
        self.assertEqual(trip_for_false_part3.is_family, False)

    def test_book_a_trip_if_destination_not_in_the_list(self):
        result = self.current_trip.book_a_trip('Germany')
        self.assertEqual(result, 'This destination is not in our offers, please choose a new one!')

    def test_book_a_trip_if_budget_is_less_than_total_price(self):
        result = self.current_trip.book_a_trip('New Zealand')
        self.assertEqual(result, 'Your budget is not enough!')
        trip = Trip(400, 10, True)
        result2 = trip.book_a_trip('New Zealand')
        self.assertEqual(result2, 'Your budget is not enough!')

    def test_book_a_trip_if_budget_is_enough_for_family_and_not(self):
        family_trip = Trip(4000, 3, True)
        result = family_trip.book_a_trip('Bulgaria')
        amount_needed = 4000 - (1500 * 0.9)
        self.assertEqual(result, f'Successfully booked destination Bulgaria! Your budget left is {amount_needed:.2f}')
        self.assertEqual(family_trip.budget, amount_needed)
        value_for_dict = 1500 * 0.9
        self.assertEqual(family_trip.booked_destinations_paid_amounts, {'Bulgaria': value_for_dict})

        not_family_trip = Trip(4000, 3, False)
        result2 = not_family_trip.book_a_trip('Bulgaria')
        amount_needed2 = 4000 - 1500
        self.assertEqual(result2, f'Successfully booked destination Bulgaria! Your budget left is {amount_needed2:.2f}')
        self.assertEqual(not_family_trip.budget, amount_needed2)
        self.assertEqual(not_family_trip.booked_destinations_paid_amounts, {'Bulgaria': 1500})

    def test_booking_status(self):
        result = self.current_trip.booking_status()
        self.assertEqual(result, f'No bookings yet. Budget: 4000.00')

        new_trip = Trip(20000, 2, False)
        new_trip.book_a_trip('Brazil')
        new_trip.book_a_trip('Bulgaria')
        result = new_trip.booking_status()
        message = f"Booked Destination: Brazil\n" \
                  f"Paid Amount: {12400:.2f}\n" \
                  f"Booked Destination: Bulgaria\n" \
                  f"Paid Amount: {1000:.2f}\n" \
                  f"Number of Travelers: 2\n" \
                  f"Budget Left: 6600.00"

        self.assertEqual(result, message)




