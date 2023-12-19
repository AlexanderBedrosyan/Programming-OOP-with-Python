from project.divers.base_diver import BaseDiver
from project.divers.free_diver import FreeDiver
from project.divers.scuba_diver import ScubaDiver
from project.fish.base_fish import BaseFish
from typing import List

from project.fish.deep_sea_fish import DeepSeaFish
from project.fish.predatory_fish import PredatoryFish


class NauticalCatchChallengeApp:

    def __init__(self):
        self.divers: List[BaseDiver] = []
        self.fish_list: List[BaseFish] = []

    @staticmethod
    def diver_type_validator(diver_type):
        type_of_divers = {
            "FreeDiver": FreeDiver,
            "ScubaDiver": ScubaDiver
        }
        if diver_type in type_of_divers:
            return type_of_divers[diver_type]

    @staticmethod
    def find_object(item: str or int, attribute: str, collection: list):
        for obj in collection:
            if getattr(obj, attribute) == item:
                return obj

    def dive_into_competition(self, diver_type: str, diver_name: str):
        if self.diver_type_validator(diver_type) is None:
            return f"{diver_type} is not allowed in our competition."

        diver_checker = self.find_object(diver_name, 'name', self.divers)

        if diver_checker:
            return f"{diver_name} is already a participant -> {diver_type}."

        new_diver = self.diver_type_validator(diver_type)(diver_name)
        self.divers.append(new_diver)
        return f"{diver_name} is successfully registered for the competition as a {diver_type}."

    @staticmethod
    def fish_type_validator(fish_type):
        type_of_fish = {
            "PredatoryFish": PredatoryFish,
            "DeepSeaFish": DeepSeaFish
        }
        if fish_type in type_of_fish:
            return type_of_fish[fish_type]

    def swim_into_competition(self, fish_type: str, fish_name: str, points: float):
        if self.fish_type_validator(fish_type) is None:
            return f"{fish_type} is forbidden for chasing in our competition."

        fish_checker = self.find_object(fish_name, 'name', self.fish_list)

        if fish_checker:
            return f"{fish_name} is already allowed as a {fish_type}."

        new_fish = self.fish_type_validator(fish_type)(fish_name, points)
        self.fish_list.append(new_fish)
        return f"{fish_name} is allowed for chasing."

    @staticmethod
    def check_if_oxygen_level_is_zero(diver):
        if diver.oxygen_level == 0:
            diver.has_health_issue = True

    def chase_fish(self, diver_name: str, fish_name: str, is_lucky: bool):
        diver = self.find_object(diver_name, 'name', self.divers)
        if diver is None:
            return f"{diver_name} is not registered for the competition."

        fish = self.find_object(fish_name, 'name', self.fish_list)
        if fish is None:
            return f"The {fish_name} is not allowed to be caught in this competition."

        if diver.has_health_issue:
            return f"{diver_name} will not be allowed to dive, due to health issues."

        if diver.oxygen_level < fish.time_to_catch:
            diver.miss(fish.time_to_catch)
            self.check_if_oxygen_level_is_zero(diver)
            return f"{diver_name} missed a good {fish_name}."

        elif diver.oxygen_level == fish.time_to_catch:
            if is_lucky:
                diver.hit(fish)
                self.check_if_oxygen_level_is_zero(diver)
            else:
                diver.miss(fish.time_to_catch)
                self.check_if_oxygen_level_is_zero(diver)
                return f"{diver_name} missed a good {fish_name}."
        else:
            diver.hit(fish)

        return f"{diver_name} hits a {fish.points}pt. {fish_name}."

    def health_recovery(self):
        count = 0
        for diver in self.divers:
            if diver.has_health_issue:
                diver.update_health_status()
                diver.renew_oxy()
                count += 1
        return f"Divers recovered: {count}"

    def diver_catch_report(self, diver_name: str):
        diver = self.find_object(diver_name, 'name', self.divers)
        result = [
            f"**{diver_name} Catch Report**"
        ]
        for fish in diver.catch:
            result.append(fish.fish_details())

        return '\n'.join(result)

    def competition_statistics(self):
        sorted_divers = list(sorted(self.divers, key=lambda diver: (-diver.competition_points, -len(diver.catch), diver.name)))
        result = [
            "**Nautical Catch Challenge Statistics**"
        ]

        for current_diver in sorted_divers:
            if not current_diver.has_health_issue:
                result.append(str(current_diver))

        return '\n'.join(result)
