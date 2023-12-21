from project import helper
from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race


class Controller:

    def __init__(self):
        self.cars: list = []
        self.drivers: list = []
        self.races: list = []

    @staticmethod
    def __valid_car_types(current_type):
        car_types = {
            "MuscleCar": MuscleCar,
            "SportsCar": SportsCar
        }
        if current_type in car_types:
            return car_types[current_type]

    def create_car(self, car_type: str, model: str, speed_limit: int):
        if helper.find_object(model, 'model', self.cars) is not None:
            raise Exception(f"Car {model} is already created!")
        if self.__valid_car_types(car_type) is None:
            return
        new_car = self.__valid_car_types(car_type)(model, speed_limit)
        self.cars.append(new_car)
        return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):
        if helper.find_object(driver_name, 'name', self.drivers) is not None:
            raise Exception(f"Driver {driver_name} is already created!")
        new_driver = Driver(driver_name)
        self.drivers.append(new_driver)
        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        if helper.find_object(race_name, 'name', self.races) is not None:
            raise Exception(f"Race {race_name} is already created!")
        new_race = Race(race_name)
        self.races.append(new_race)
        return f"Race {race_name} is created."

    def find_car_from_the_last_added_by_type(self, car_type):
        for car in self.cars[::-1]:
            if car.__class__.__name__ == car_type and not car.is_taken:
                return car

    def add_car_to_driver(self, driver_name: str, car_type: str):
        current_car = self.find_car_from_the_last_added_by_type(car_type)
        driver = helper.find_object(driver_name, 'name', self.drivers)

        if driver is None:
            raise Exception(f"Driver {driver_name} could not be found!")

        if current_car is None:
            raise Exception(f"Car {car_type} could not be found!")

        if driver.car is not None:
            old_model = driver.car
            driver.car = current_car
            current_car.is_taken = True
            old_model.is_taken = False
            return f"Driver {driver_name} changed his car from {old_model.model} to {current_car.model}."

        driver.car = current_car
        current_car.is_taken = True
        return f"Driver {driver_name} chose the car {current_car.model}."

    def add_driver_to_race(self, race_name: str, driver_name: str):
        driver = helper.find_object(driver_name, 'name', self.drivers)
        race = helper.find_object(race_name, 'name', self.races)

        if race is None:
            raise Exception(f"Race {race_name} could not be found!")

        if driver is None:
            raise Exception(f"Driver {driver_name} could not be found!")

        if driver.car is None:
            raise Exception(f"Driver {driver_name} could not participate in the race!")

        if driver in race.drivers:
            return f"Driver {driver_name} is already added in {race_name} race."

        race.drivers.append(driver)
        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str):
        race = helper.find_object(race_name, 'name', self.races)

        if race is None:
            raise Exception(f"Race {race_name} could not be found!")

        if len(race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")

        result = []

        sorted_race_list = list(sorted(race.drivers, key=lambda x: -x.car.speed_limit))

        for i in range(3):
            speed_limit = sorted_race_list[i].car.speed_limit
            result.append(f"Driver {sorted_race_list[i].name} wins the {race_name} race with a speed of {speed_limit}.")
            sorted_race_list[i].number_of_wins += 1

        return '\n'.join(result)
