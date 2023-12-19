from project.divers.base_diver import BaseDiver


class FreeDiver(BaseDiver):

    def __init__(self, name: str):
        super().__init__(name, 120)

    @property
    def original_oxygen_level(self):
        return 120

    def miss(self, time_to_catch: int):
        reduce_level = time_to_catch * 0.6
        if self.oxygen_level - reduce_level < 0:
            self.oxygen_level = 0
        else:
            self.oxygen_level = round(self.oxygen_level - reduce_level)

    def renew_oxy(self):
        self.oxygen_level = self.original_oxygen_level
