from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription
from project.trainer import Trainer


class Gym:

    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    @staticmethod
    def find_object(item: str or int, attribute: str, collection: list):
        for obj in collection:
            if getattr(obj, attribute) == item:
                return obj

    def add_customer(self, customer: Customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int):
        subscription = Gym.find_object(subscription_id, 'id', self.subscriptions)
        customer = Gym.find_object(subscription.customer_id, 'id', self.customers)
        trainer = Gym.find_object(subscription.trainer_id, 'id', self.trainers)
        plan = Gym.find_object(subscription.exercise_id, 'id', self.plans)
        equipment = Gym.find_object(plan.equipment_id, 'id', self.equipment)
        result = [
            subscription.__repr__(),
            customer.__repr__(),
            trainer.__repr__(),
            equipment.__repr__(),
            plan.__repr__()
        ]
        return '\n'.join(result)