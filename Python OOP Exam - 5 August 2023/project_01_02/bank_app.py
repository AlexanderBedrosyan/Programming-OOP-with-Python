from project.clients.adult import Adult
from project.clients.student import Student
from project.loans.mortgage_loan import MortgageLoan
from project.loans.student_loan import StudentLoan


class BankApp:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.loans: list = []
        self.clients: list = []

    @staticmethod
    def valid_loans(loan_type):
        loans = {
            "StudentLoan": StudentLoan,
            "MortgageLoan": MortgageLoan
        }
        if loan_type in loans:
            return loans[loan_type]

    @staticmethod
    def valid_clients(client_type):
        clients = {
            "Student": Student,
            "Adult": Adult
        }
        if client_type in clients:
            return clients[client_type]

    def add_loan(self, loan_type: str):
        if self.valid_loans(loan_type) is None:
            raise Exception("Invalid loan type!")
        new_loan = self.valid_loans(loan_type)()
        self.loans.append(new_loan)
        return f"{loan_type} was successfully added."

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float):
        if self.valid_clients(client_type) is None:
            raise Exception("Invalid client type!")
        if self.capacity <= len(self.clients):
            return "Not enough bank capacity."
        new_client = self.valid_clients(client_type)(client_name, client_id, income)
        self.clients.append(new_client)
        return f"{client_type} was successfully added."

    @staticmethod
    def find_object(item: str or int, attribute: str, collection: list):
        for obj in collection:
            if getattr(obj, attribute) == item:
                return obj

    @staticmethod
    def find_objects_by_type(objects_list, type_needed):
        for obj in objects_list:
            if obj.__class__.__name__ == type_needed:
                return obj

    def grant_loan(self, loan_type: str, client_id: str):
        valid_combinations = {
            'StudentLoan': 'Student',
            'MortgageLoan': 'Adult'
        }
        loan_for_adding = self.find_objects_by_type(self.loans, loan_type)
        current_client = self.find_object(client_id, 'client_id', self.clients)
        if valid_combinations[loan_type] != current_client.__class__.__name__:
            raise Exception("Inappropriate loan type!")
        current_client.loans.append(loan_for_adding)
        self.loans.remove(loan_for_adding)
        return f"Successfully granted {loan_type} to {current_client.name} with ID {client_id}."

    def remove_client(self, client_id: str):
        if self.find_object(client_id, 'client_id', self.clients) is None:
            raise Exception("No such client!")

        client_found = self.find_object(client_id, 'client_id', self.clients)

        if len(client_found.loans) > 0:
            raise Exception("The client has loans! Removal is impossible!")

        self.clients.remove(client_found)
        return f"Successfully removed {client_found.name} with ID {client_id}."

    def increase_loan_interest(self, loan_type: str):
        number_of_changed_loans = 0

        for loan in self.loans:
            if loan.__class__.__name__ == loan_type:
                loan.increase_interest_rate()
                number_of_changed_loans += 1

        return f"Successfully changed {number_of_changed_loans} loans."

    def increase_clients_interest(self, min_rate: float):
        changed_client_rates_number = 0

        for client in self.clients:
            if client.interest < min_rate:
                client.increase_clients_interest()
                changed_client_rates_number += 1

        return f"Number of clients affected: {changed_client_rates_number}."

    @property
    def total_clients_income(self):
        return sum([client.income for client in self.clients])

    @property
    def loans_count_granted_to_clients(self):
        counter_of_loans = 0
        total_sum_of_loans = 0
        for client in self.clients:
            counter_of_loans += len(client.loans)
            for loan in client.loans:
                total_sum_of_loans += loan.amount
        return counter_of_loans, total_sum_of_loans

    @property
    def avg_client_interest_rate(self):
        if self.clients:
            total_interests = 0
            for client in self.clients:
                total_interests += client.interest
            return total_interests / len(self.clients)
        else:
            return 0

    def get_statistics(self):
        result = [
            f"Active Clients: {len(self.clients)}",
            f"Total Income: {self.total_clients_income:.2f}",
            f"Granted Loans: {self.loans_count_granted_to_clients[0]}, Total Sum: {self.loans_count_granted_to_clients[1]:.2f}",
            f"Available Loans: {len(self.loans)}, Total Sum: {sum([loan.amount for loan in self.loans]):.2f}",
            f"Average Client Interest Rate: {self.avg_client_interest_rate:.2f}"
        ]
        return '\n'.join(result)
