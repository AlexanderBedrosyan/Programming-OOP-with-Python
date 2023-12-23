from project.vehicles.base_vehicle import BaseVehicle


class PassengerCar(BaseVehicle):
    MAX_MILEAGE = 450.00

    def __init__(self, brand: str, model: str, license_plate_number: str):
        super().__init__(brand, model, license_plate_number, PassengerCar.MAX_MILEAGE)

    def drive(self, mileage:float):
        percentage = 0
        if PassengerCar.MAX_MILEAGE >= mileage:
            percentage = round((mileage / PassengerCar.MAX_MILEAGE) * 100)
        else:
            percentage = round(PassengerCar.MAX_MILEAGE)
        self.battery_level -= percentage