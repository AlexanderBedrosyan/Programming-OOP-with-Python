from project import helper
from project.client import Client
from project.meals.meal import Meal
from project.meals.dessert import Dessert
from project.meals.starter import Starter
from project.meals.main_dish import MainDish


class FoodOrdersApp:
    RECEIPT_ID = 0

    def __init__(self):
        self.menu: list = []
        self.clients_list: list = []

    def register_client(self, client_phone_number: str):
        if helper.find_object(client_phone_number, 'phone_number', self.clients_list) is not None:
            raise Exception("The client has already been registered!")
        new_client = Client(client_phone_number)
        self.clients_list.append(new_client)
        return f"Client {client_phone_number} registered successfully."

    @staticmethod
    def valid_meals():
        return ["Starter", "MainDish", "Dessert"]

    def add_meals_to_menu(self, *meals: Meal):
        for meal in meals:
            if meal.__class__.__name__ not in self.valid_meals():
                continue
            self.menu.append(meal)

    def show_menu(self):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

        meals_information = []

        for meal in self.menu:
            meals_information.append(meal.details())

        return '\n'.join(meals_information)

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

        client = helper.find_object(client_phone_number, 'phone_number', self.clients_list)

        if client is None:
            client = Client(client_phone_number)
            self.clients_list.append(client)

        current_client_order = []

        for meal_name, quantity in meal_names_and_quantities.items():
            if meal_name not in [meal.name for meal in self.menu]:
                raise Exception(f"{meal_name} is not on the menu!")

            current_meal = helper.find_object(meal_name, 'name', self.menu)

            if quantity > current_meal.quantity:
                raise Exception(f"Not enough quantity of {current_meal.__class__.__name__}: {meal_name}!")

            current_client_order.append(current_meal)

        for meal in current_client_order:
            name_of_meal = meal.name
            needed_quantity = meal_names_and_quantities[name_of_meal]

            if name_of_meal not in client.ORDERS:
                client.ORDERS[name_of_meal] = 0
            client.ORDERS[name_of_meal] += needed_quantity

            client.bill += (needed_quantity * meal.price)
            meal.quantity -= needed_quantity
            client.shopping_cart.append(meal)

        meal_names = [ordered_meal.name for ordered_meal in client.shopping_cart]
        return f"Client {client_phone_number} successfully ordered {', '.join(meal_names)} for {client.bill:.2f}lv."

    def cancel_order(self, client_phone_number: str):
        client = helper.find_object(client_phone_number, 'phone_number', self.clients_list)

        if len(client.shopping_cart) <= 0:
            raise Exception(f"There are no ordered meals!")

        for meal in client.shopping_cart:
            name_of_meal = meal.name
            meal.quantity += client.ORDERS[name_of_meal]

        client.ORDERS = {}
        client.shopping_cart = []
        client.bill = 0

        return f"Client {client_phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number: str):
        client = helper.find_object(client_phone_number, 'phone_number', self.clients_list)

        if len(client.shopping_cart) <= 0:
            raise Exception("There are no ordered meals!")

        FoodOrdersApp.RECEIPT_ID += 1
        total_amount_of_bill = client.bill
        client.bill = 0
        client.ORDERS = {}
        client.shopping_cart = []
        return f"Receipt #{FoodOrdersApp.RECEIPT_ID} with total amount of {total_amount_of_bill:.2f} was successfully paid for {client_phone_number}."

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."

