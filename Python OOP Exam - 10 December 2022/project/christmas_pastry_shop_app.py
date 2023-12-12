from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen


class ChristmasPastryShopApp:

    def __init__(self):
        self.booths: list = []
        self.delicacies: list = []
        self.income: float = 0.0

    @staticmethod
    def valid_delicacy(type_delicacy):
        valid_types = {
            "Gingerbread": Gingerbread,
            "Stolen": Stolen
        }
        if type_delicacy in valid_types:
            return valid_types[type_delicacy]

    @staticmethod
    def find_object(item: str or int, attribute: str, collection: list):
        for obj in collection:
            if getattr(obj, attribute) == item:
                return obj

    @staticmethod
    def valid_booths(booth_type):
        valid_booths = {
            "Open Booth": OpenBooth,
            "Private Booth": PrivateBooth
        }
        if booth_type in valid_booths:
            return valid_booths[booth_type]

    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        if self.find_object(name, 'name', self.delicacies) is not None:
            raise Exception(f"{name} already exists!")
        if self.valid_delicacy(type_delicacy) is None:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")

        new_delicacy = self.valid_delicacy(type_delicacy)(name, price)
        self.delicacies.append(new_delicacy)
        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        if self.find_object(booth_number, 'booth_number', self.booths) is not None:
            raise Exception(f"Booth number {booth_number} already exists!")
        if self.valid_booths(type_booth) is None:
            raise Exception(f"{type_booth} is not a valid booth!")

        new_booth = self.valid_booths(type_booth)(booth_number, capacity)
        self.booths.append(new_booth)

        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int):
        for booth in self.booths:
            if booth.capacity >= number_of_people and not booth.is_reserved:
                booth.reserve(number_of_people)
                return f"Booth {booth.booth_number} has been reserved for {number_of_people} people."
        raise Exception(f"No available booth for {number_of_people} people!")

    def order_delicacy(self, booth_number: int, delicacy_name: str):
        booth = self.find_object(booth_number, 'booth_number', self.booths)
        if booth is None:
            raise Exception(f"Could not find booth {booth_number}!")

        delicacy = self.find_object(delicacy_name, 'name', self.delicacies)
        if delicacy is None:
            raise Exception(f"No {delicacy_name} in the pastry shop!")

        booth.delicacy_orders.append(delicacy)
        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number: int):
        booth = self.find_object(booth_number, 'booth_number', self.booths)
        bill = (booth.price_for_reservation + sum([order.price for order in booth.delicacy_orders]))
        self.income += bill
        booth.delicacy_orders = []
        booth.price_for_reservation = 0
        booth.is_reserved = False
        return f'Booth {booth.booth_number}:\nBill: {bill:.2f}lv.'

    def get_income(self):
        return f"Income: {self.income:.2f}lv."
