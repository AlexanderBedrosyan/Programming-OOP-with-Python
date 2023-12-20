from project.teams.base_team import BaseTeam


class OutdoorTeam(BaseTeam):

    def __init__(self, name, country, advantage):
        super().__init__(name, country, advantage, 1000)

    def win(self):
        self.advantage += 115
        self.wins += 1
