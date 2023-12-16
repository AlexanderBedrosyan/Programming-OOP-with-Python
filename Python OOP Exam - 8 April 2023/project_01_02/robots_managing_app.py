from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:

    def __init__(self):
        self.robots: list = []
        self.services: list = []

    @staticmethod
    def valid_services(current_type):
        services = {
            "MainService": MainService,
            "SecondaryService": SecondaryService
        }
        if current_type in services:
            return services[current_type]

    @staticmethod
    def valid_robot(current_type):
        robots = {
            "MaleRobot": MaleRobot,
            "FemaleRobot": FemaleRobot
        }
        if current_type in robots:
            return robots[current_type]

    @staticmethod
    def find_object(item: str or int, attribute: str, collection: list):
        for obj in collection:
            if getattr(obj, attribute) == item:
                return obj

    def add_service(self, service_type: str, name: str):
        if self.valid_services(service_type) is None:
            raise Exception("Invalid service type!")

        new_service = self.valid_services(service_type)(name)
        self.services.append(new_service)
        return f"{service_type} is successfully added."

    def add_robot(self, robot_type: str, name: str, kind: str, price: float):
        if self.valid_robot(robot_type) is None:
            raise Exception("Invalid robot type!")

        new_robot = self.valid_robot(robot_type)(name, kind, price)
        self.robots.append(new_robot)
        return f"{robot_type} is successfully added."

    @staticmethod
    def robot_checker(robot_name):
        robots = {
            "MaleRobot": 'MainService',
            "FemaleRobot": 'SecondaryService'
        }
        return robots[robot_name]

    def add_robot_to_service(self, robot_name: str, service_name: str):
        robot = self.find_object(robot_name, 'name', self.robots)
        service = self.find_object(service_name, 'name', self.services)

        if self.robot_checker(robot.__class__.__name__) != service.__class__.__name__:
            return f"Unsuitable service."

        if service.capacity <= len(service.robots):
            raise Exception("Not enough capacity for this robot!")

        self.robots.remove(robot)
        service.robots.append(robot)
        return f"Successfully added {robot_name} to {service_name}."

    def remove_robot_from_service(self, robot_name: str, service_name: str):
        needed_service = self.find_object(service_name, 'name', self.services)
        robot = self.find_object(robot_name, 'name', needed_service.robots)

        if robot is None:
            raise Exception("No such robot in this service!")

        needed_service.robots.remove(robot)
        self.robots.append(robot)

        return f"Successfully removed {robot_name} from {service_name}."

    def feed_all_robots_from_service(self, service_name: str):
        service = self.find_object(service_name, 'name', self.services)
        fed_robots_counter = 0

        for robot in service.robots:
            robot.eating()
            fed_robots_counter += 1

        return f"Robots fed: {fed_robots_counter}."

    def service_price(self, service_name: str):
        total_price = 0
        service = self.find_object(service_name, 'name', self.services)
        for robot in service.robots:
            total_price += robot.price

        return f"The value of service {service_name} is {total_price:.2f}."

    def __str__(self):
        result = []
        for service in self.services:
            result.append(service.details())
        return '\n'.join(result)
