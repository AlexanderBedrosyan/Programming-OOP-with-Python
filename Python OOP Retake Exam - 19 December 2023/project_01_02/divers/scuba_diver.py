from project.divers.base_diver import BaseDiver


class ScubaDiver(BaseDiver):
    __ORIGINAL_OXYGEN_LEVEL = 540

    def __init__(self, name: str):
        super().__init__(name, 540)

    @property
    def original_oxygen_level(self):
        return 540

    def miss(self, time_to_catch: int):
        reduce_level = time_to_catch * 0.3
        if self.oxygen_level - reduce_level < 0:
            self.oxygen_level = 0
        else:
            self.oxygen_level = round(self.oxygen_level - reduce_level)

    def renew_oxy(self):
        self.oxygen_level = self.original_oxygen_level