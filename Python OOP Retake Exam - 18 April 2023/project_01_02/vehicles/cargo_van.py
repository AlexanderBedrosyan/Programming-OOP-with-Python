from project.vehicles.base_vehicle import BaseVehicle


class CargoVan(BaseVehicle):
    MAX_MILEAGE = 180

    def __init__(self, brand: str, model: str, license_plate_number: str):
        super().__init__(brand, model, license_plate_number, CargoVan.MAX_MILEAGE)

    def drive(self, mileage: float):
        percentage = 0
        if CargoVan.MAX_MILEAGE >= mileage:
            percentage = round((mileage / CargoVan.MAX_MILEAGE + 0.05) * 100)
        else:
            percentage = round(CargoVan.MAX_MILEAGE)
        self.battery_level -= percentage
