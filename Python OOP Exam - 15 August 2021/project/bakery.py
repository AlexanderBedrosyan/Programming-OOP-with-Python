from project.baked_food.baked_food import BakedFood
from typing import List

from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.drink import Drink
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable
from project.table.table import Table


class Bakery:

    def __init__(self, name:str):
        self.name = name
        self.food_menu: List[BakedFood] = []
        self.drinks_menu: List[Drink] = []
        self.tables_repository: List[Table] = []
        self.total_income = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == '' or value.isspace():
            raise ValueError("Name cannot be empty string or white space!")
        self.__name = value

    @staticmethod
    def food_types_validator(food_type):
        types_of_food = {
            "Bread": Bread,
            "Cake": Cake
        }
        if food_type in types_of_food:
            return types_of_food[food_type]

    @staticmethod
    def find_objects_by_name(objects_list, name):
        for obj in objects_list:
            if obj.name == name:
                return obj

    @staticmethod
    def drink_types_validator(drink_type):
        types_of_drinks = {
            "Tea": Tea,
            "Water": Water,
        }
        if drink_type in types_of_drinks:
            return types_of_drinks[drink_type]

    @staticmethod
    def table_types_validator(table_type):
        types_of_tables = {
            "InsideTable": InsideTable,
            "OutsideTable": OutsideTable
        }
        if table_type in types_of_tables:
            return types_of_tables[table_type]

    def find_table_by_number(self, table_number):
        for table in self.tables_repository:
            if table.table_number == table_number:
                return table

    def add_food(self, food_type: str, name: str, price: float):
        if self.find_objects_by_name(self.food_menu, name) is not None:
            raise Exception(f"{food_type} {name} is already in the menu!")

        if self.food_types_validator(food_type) is None:
            return

        new_food = self.food_types_validator(food_type)(name, price)
        self.food_menu.append(new_food)
        return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type: str, name: str, portion: float, brand:str):
        if self.find_objects_by_name(self.drinks_menu, name) is not None:
            raise Exception(f"{drink_type} {name} is already in the menu!")

        if self.drink_types_validator(drink_type) is None:
            return

        new_drink = self.drink_types_validator(drink_type)(name, portion, brand)
        self.drinks_menu.append(new_drink)
        return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_type: str, table_number: int, capacity: int):
        if self.find_table_by_number(table_number) is not None:
            raise Exception(f"Table {table_number} is already in the bakery!")

        if self.table_types_validator(table_type) is None:
            return

        new_table = self.table_types_validator(table_type)(table_number, capacity)
        self.tables_repository.append(new_table)
        return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people: int):
        for table in self.tables_repository:
            if not table.is_reserved and table.capacity >= number_of_people:
                table.reserve(number_of_people)
                return f"Table {table.table_number} has been reserved for {number_of_people} people"
        return f"No available table for {number_of_people} people"

    def order_food(self, table_number: int, *foods):
        table = self.find_table_by_number(table_number)
        if table is None:
            return f"Could not find table {table_number}"

        ordered_result = [
            f'Table {table_number} ordered:'
        ]

        not_in_the_menu_result = [
            f'{self.name} does not have in the menu:'
        ]

        for food_name in foods:
            food = self.find_objects_by_name(self.food_menu, food_name)
            if food is None:
                not_in_the_menu_result.append(f'{food_name}')
                continue

            ordered_result.append(food.__repr__())
            table.order_food(food)
            self.total_income += food.price

        for element in not_in_the_menu_result:
            ordered_result.append(element)

        return '\n'.join(ordered_result)

    def order_drink(self, table_number: int, *drinks):
        table = self.find_table_by_number(table_number)
        if table is None:
            return f"Could not find table {table_number}"

        ordered_result = [
            f'Table {table_number} ordered:'
        ]

        not_in_the_menu_result = [
            f'{self.name} does not have in the menu:'
        ]

        for drink_name in drinks:
            drink = self.find_objects_by_name(self.drinks_menu, drink_name)
            if drink is None:
                not_in_the_menu_result.append(f"{drink_name}")
                continue

            ordered_result.append(drink.__repr__())
            table.order_drink(drink)
            self.total_income += drink.price

        result = ordered_result + not_in_the_menu_result
        return '\n'.join(result)

    def leave_table(self, table_number: int):
        table = self.find_table_by_number(table_number)
        if table:
            bill = table.get_bill()
            table.clear()
            return f"Table: {table_number}\nBill: {bill:.2f}"

    def get_free_tables_info(self):
        result = []
        for table in self.tables_repository:
            free_table = table.free_table_info()
            if free_table is not None:
                result.append(free_table)
        return '\n'.join(result)

    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}lv"
