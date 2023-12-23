from project.route import Route
from project.user import User
from project.vehicles.base_vehicle import BaseVehicle
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar


class ManagingApp:

    def __init__(self):
        self.users = []
        self.vehicles = []
        self.routes = []

    def car_types(self, element):
        type_of_cars = {
            "PassengerCar": PassengerCar,
            "CargoVan": CargoVan,
        }
        return type_of_cars[element]

    def register_user(self, first_name: str, last_name: str, driving_license_number: str):
        for ch in self.users:
            if ch.driving_license_number == driving_license_number:
                return f"{driving_license_number} has already been registered to our platform."
        current_user = User(first_name, last_name, driving_license_number)
        self.users.append(current_user)
        return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):
        if vehicle_type != "PassengerCar" and vehicle_type != "CargoVan":
            return f"Vehicle type {vehicle_type} is inaccessible."
        for ch in self.vehicles:
            if ch.license_plate_number == license_plate_number:
                return f"{license_plate_number} belongs to another vehicle."
        new_vehicle = self.car_types(vehicle_type)(brand, model, license_plate_number)
        self.vehicles.append(new_vehicle)
        return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

    def allow_route(self, start_point: str, end_point: str, length: float):
        for ch in self.routes:
            if ch.start_point == start_point and ch.end_point == end_point and ch.length == length:
                return f"{start_point}/{end_point} - {length} km had already been added to our platform."
            if ch.start_point == start_point and ch.end_point == end_point and ch.length < length:
                return f"{start_point}/{end_point} shorter route had already been added to our platform."
            if ch.start_point == start_point and ch.end_point == end_point and ch.length > length:
                ch.is_locked = True
        new_route = Route(start_point, end_point, length, (len(self.routes) + 1))
        self.routes.append(new_route)
        return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

    def make_trip(self, driving_license_number: str, license_plate_number: str, route_id: int,
                  is_accident_happened: bool):

        needed_vehicle = []
        needed_route = []
        needed_user = []
        for ch in self.users:
            if ch.driving_license_number == driving_license_number:
                if ch.is_blocked:
                    return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."
                else:
                    needed_user.append(ch)

        for vehicle in self.vehicles:
            if vehicle.license_plate_number == license_plate_number:
                if vehicle.is_damaged:
                    return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."
                else:
                    needed_vehicle.append(vehicle)

        for route in self.routes:
            if route.route_id == route_id:
                if route.is_locked:
                    return f"Route {route_id} is locked! This trip is not allowed."
                else:
                    needed_route.append(route)

        needed_vehicle[0].drive(needed_route[0].length)

        if is_accident_happened:
            needed_vehicle[0].is_damaged = True
            needed_user[0].decrease_rating()
        else:
            needed_user[0].increase_rating()

        return needed_vehicle[0].__str__()

    def repair_vehicles(self, count: int):
        damaged_cars = [c for c in self.vehicles if c.is_damaged]

        sorted_cars = sorted(damaged_cars, key=lambda c: (c.brand, c.model))[:count]
        for car in sorted_cars:
            car.recharge()
            car.change_status()

        return f"{len(sorted_cars)} vehicles were successfully repaired!"

    def users_report(self):
        result = ["*** E-Drive-Rent ***"]
        sorted_users = sorted(self.users, key=lambda user: -user.rating)
        for user in sorted_users:
            result.append(user.__str__())
        return '\n'.join(result)


# app = ManagingApp()
# print(app.register_user('Tisha', 'Reenie', '7246506' ))
# print(app.register_user('Bernard', 'Remy', 'CDYHVSR68661'))
# print(app.register_user('Mack', 'Cindi', '7246506'))
# print(app.upload_vehicle('PassengerCar', 'Chevrolet', 'Volt', 'CWP8032'))
# print(app.upload_vehicle('PassengerCar', 'Volkswagen', 'e-Up!', 'COUN199728'))
# print(app.upload_vehicle('PassengerCar', 'Mercedes-Benz', 'EQS', '5UNM315'))
# print(app.upload_vehicle('CargoVan', 'Ford', 'e-Transit', '726QOA'))
# print(app.upload_vehicle('CargoVan', 'BrightDrop', 'Zevo400', 'SC39690'))
# print(app.upload_vehicle('EcoTruck', 'Mercedes-Benz', 'eActros', 'SC39690'))
# print(app.upload_vehicle('PassengerCar', 'Tesla', 'CyberTruck', '726QOA'))
# print(app.allow_route('SOF', 'PLD', 144))
# print(app.allow_route('BUR', 'VAR', 87))
# print(app.allow_route('BUR', 'VAR', 87))
# print(app.allow_route('SOF', 'PLD', 184))
# print(app.allow_route('BUR', 'VAR', 86.999))
# print(app.make_trip('CDYHVSR68661', '5UNM315', 3, False))
# print(app.make_trip('7246506', 'CWP8032', 1, True))
# print(app.make_trip('7246506', 'COUN199728', 1, False))
# print(app.make_trip('CDYHVSR68661', 'CWP8032', 3, False))
# print(app.make_trip('CDYHVSR68661', '5UNM315', 2, False))
# print(app.repair_vehicles(2))
# print(app.repair_vehicles(20))
# print(app.users_report())
