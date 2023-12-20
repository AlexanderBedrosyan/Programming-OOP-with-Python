from typing import List

from project.equipment.elbow_pad import ElbowPad
from project.equipment.knee_pad import KneePad
from project.teams.indoor_team import IndoorTeam
from project.teams.outdoor_team import OutdoorTeam
from project import helper


class Tournament:

    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.equipment: List[ElbowPad, KneePad] = []
        self.teams: List[IndoorTeam, OutdoorTeam] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        message = "Tournament name should contain letters and digits only!"
        helper.value_error_if_string_is_not_only_with_letters_and_digits(value, message)
        self.__name = value

    @staticmethod
    def __valid_types(current_type):
        types = {
            "KneePad": KneePad,
            "ElbowPad": ElbowPad
        }
        if current_type in types:
            return types[current_type]

    @staticmethod
    def __valid_teams(current_team):
        teams = {
            "OutdoorTeam": OutdoorTeam,
            "IndoorTeam": IndoorTeam
        }
        if current_team in teams:
            return teams[current_team]

    def add_equipment(self, equipment_type: str):
        if self.__valid_types(equipment_type) is None:
            raise Exception(f"Invalid equipment type!")
        new_equipment = self.__valid_types(equipment_type)()
        self.equipment.append(new_equipment)
        return f"{equipment_type} was successfully added."

    def add_team(self, team_type: str, team_name: str, country: str, advantage: int):
        if self.__valid_teams(team_type) is None:
            raise Exception("Invalid team type!")
        if self.capacity <= len(self.teams):
            return f"Not enough tournament capacity."
        new_team = self.__valid_teams(team_type)(team_name, country, advantage)
        self.teams.append(new_team)
        return f"{team_type} was successfully added."

    def __find_equipment_by_type(self, current_type):
        for equip in self.equipment[::-1]:
            if equip.__class__.__name__ == current_type:
                return equip

    def sell_equipment(self, equipment_type: str, team_name: str):
        equipment = self.__find_equipment_by_type(equipment_type)
        team = helper.find_object(team_name, 'name', self.teams)
        if team.budget < equipment.price:
            raise Exception("Budget is not enough!")
        team.equipment.append(equipment)
        team.budget -= equipment.price
        for i in range(len(self.equipment) - 1, - 1, - 1):
            if self.equipment[i] == equipment:
                self.equipment.pop(i)
                break
        return f"Successfully sold {equipment_type} to {team_name}."

    def remove_team(self, team_name: str):
        team = helper.find_object(team_name, 'name', self.teams)
        if team is None:
            raise Exception("No such team!")
        if team.wins > 0:
            raise Exception(f"The team has {team.wins} wins! Removal is impossible!")
        self.teams.remove(team)
        return f"Successfully removed {team_name}."

    def increase_equipment_price(self, equipment_type: str):
        count = 0
        for equip in self.equipment:
            if equip.__class__.__name__ == equipment_type:
                count += 1
                equip.increase_price()
        return f"Successfully changed {count}pcs of equipment."

    def play(self, team_name1: str, team_name2: str):
        team1 = helper.find_object(team_name1, 'name', self.teams)
        team2 = helper.find_object(team_name2, 'name', self.teams)
        if team1.__class__.__name__ != team2.__class__.__name__:
            raise Exception("Game cannot start! Team types mismatch!")

        first_team_advantage_and_protection = team1.advantage + sum([equip.protection for equip in team1.equipment])
        second_team_advantage_and_protection = team2.advantage + sum([equip.protection for equip in team2.equipment])
        if first_team_advantage_and_protection == second_team_advantage_and_protection:
            return f"No winner in this game."

        winner = None
        if first_team_advantage_and_protection > second_team_advantage_and_protection:
            winner = team1
        else:
            winner = team2

        winner.win()
        return f"The winner is {winner.name}."

    def get_statistics(self):
        result = [
            f"Tournament: {self.name}",
            f"Number of Teams: {len(self.teams)}",
            f"Teams:"
        ]
        sorted_teams = list(sorted(self.teams, key=lambda x: -x.wins))
        for team in sorted_teams:
            result.append(team.get_statistics())
        return '\n'.join(result)
