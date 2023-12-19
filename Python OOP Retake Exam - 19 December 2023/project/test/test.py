from project.railway_station import RailwayStation
import unittest
from collections import deque


class Test(unittest.TestCase):

    def setUp(self):
        self.railway_station = RailwayStation('London')

    def test___init___(self):
        self.assertEqual(self.railway_station.name, 'London')
        self.assertEqual(self.railway_station.arrival_trains, deque())
        self.assertEqual(self.railway_station.departure_trains, deque())
        self.assertEqual(len(self.railway_station.arrival_trains), 0)
        self.assertEqual(len(self.railway_station.departure_trains), 0)

    def test_name___setter(self):
        with self.assertRaises(ValueError) as ve:
            self.railway_station.name = 'GO'
        self.assertEqual(str(ve.exception), "Name should be more than 3 symbols!")

        self.railway_station.name = 'NewName'
        self.assertEqual(self.railway_station.name, 'NewName')

    def test_method__new_arrival_on_board(self):
        self.railway_station.new_arrival_on_board('Express train')
        self.assertEqual(self.railway_station.arrival_trains, deque(['Express train']))
        self.assertEqual(len(self.railway_station.arrival_trains), 1)

        self.railway_station.new_arrival_on_board('Passenger train')
        self.assertEqual(self.railway_station.arrival_trains, deque(['Express train', 'Passenger train']))
        self.assertEqual(len(self.railway_station.arrival_trains), 2)

    def test_method__train_has_arrived(self):
        self.railway_station.new_arrival_on_board('Express train')
        self.railway_station.new_arrival_on_board('Passenger train')
        result = self.railway_station.train_has_arrived('Rapid transit')
        self.assertEqual(result, f"There are other trains to arrive before Rapid transit.")
        self.assertEqual(len(self.railway_station.arrival_trains), 2)
        self.assertEqual(self.railway_station.arrival_trains, deque(['Express train', 'Passenger train']))
        self.assertEqual(len(self.railway_station.departure_trains), 0)
        self.assertEqual(self.railway_station.departure_trains, deque())

        result1 = self.railway_station.train_has_arrived('Express train')
        self.assertEqual(result1, f"Express train is on the platform and will leave in 5 minutes.")
        self.assertEqual(self.railway_station.arrival_trains, deque(['Passenger train']))
        self.assertEqual(len(self.railway_station.arrival_trains), 1)
        self.assertEqual(self.railway_station.departure_trains, deque(['Express train']))
        self.assertEqual(len(self.railway_station.departure_trains), 1)

        self.railway_station.arrival_trains = deque()
        self.assertEqual(self.railway_station.arrival_trains, deque())
        with self.assertRaises(IndexError) as ie:
            self.railway_station.train_has_arrived('Rapid transit')
        self.assertEqual(str(ie.exception), f"pop from an empty deque")

    def test_method__train_has_left(self):
        result = self.railway_station.train_has_left('Express train')
        self.assertEqual(result, False)

        self.railway_station.departure_trains = deque(['Express train', 'Rapid transit'])
        result2 = self.railway_station.train_has_left('Express train')
        self.assertEqual(len(self.railway_station.departure_trains), 1)
        self.assertEqual(result2, True)
        self.assertEqual(self.railway_station.departure_trains, deque(['Rapid transit']))

        result3 = self.railway_station.train_has_left('Passenger traint')
        self.assertEqual(result3, False)
        self.assertEqual(self.railway_station.departure_trains, deque(['Rapid transit']))
        self.assertEqual(len(self.railway_station.departure_trains), 1)
