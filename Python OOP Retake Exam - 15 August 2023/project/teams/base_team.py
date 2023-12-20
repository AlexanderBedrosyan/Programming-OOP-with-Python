import math
from abc import ABC, abstractmethod
from typing import List

from project import helper
from project.equipment.elbow_pad import ElbowPad
from project.equipment.knee_pad import KneePad


class BaseTeam(ABC):

    def __init__(self, name: str, country: str, advantage: int, budget: float):
        self.name = name
        self.country = country
        self.advantage = advantage
        self.budget = budget
        self.wins: int = 0
        self.equipment: List[ElbowPad, KneePad] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.isspace() or value == '':
            raise ValueError("Team name cannot be empty!")
        self.__name = value

    @property
    def country(self):
        return self.__country

    @country.setter
    def country(self, value):
        message = "Team country should be at least 2 symbols long!"
        helper.value_error_if_number_is_less_than_other_number(len(value), 2, message)
        helper.value_error_if_value_contains_only_white_spaces(value, message)
        self.__country = value

    @property
    def advantage(self):
        return self.__advantage

    @advantage.setter
    def advantage(self, value):
        if value <= 0:
            raise ValueError("Advantage must be greater than zero!")
        self.__advantage = value

    @abstractmethod
    def win(self):
        pass

    def get_statistics(self):
        total_price_of_team_equipment = sum([equip.price for equip in self.equipment])
        avg_team_protection = math.floor(sum([equip.protection for equip in self.equipment]) / len(self.equipment)) if self.equipment else 0
        return f"Name: {self.name}\n" \
               f"Country: {self.country}\n" \
               f"Advantage: {self.advantage} points\n" \
               f"Budget: {self.budget:.2f}EUR\n" \
               f"Wins: {self.wins}\n" \
               f"Total Equipment Price: {total_price_of_team_equipment:.2f}\n" \
               f"Average Protection: {int(avg_team_protection)}"
