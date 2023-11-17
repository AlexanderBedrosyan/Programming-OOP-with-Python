from project.vehicle import Vehicle


class Car(Vehicle):
    DEFAULT_FUEL_CONSUMPTION = 3

    def __init__(self, fuel, horse_power):
        super().__init__(fuel, horse_power)

    def drive(self, kilometers):
        current_fuel_consumption = kilometers * self.fuel_consumption
        if self.fuel >= current_fuel_consumption:
            self.fuel -= current_fuel_consumption