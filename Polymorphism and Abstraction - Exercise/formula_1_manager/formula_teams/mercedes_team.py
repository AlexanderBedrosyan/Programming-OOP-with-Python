from project.formula_teams.formula_team import FormulaTeam


class MercedesTeam(FormulaTeam):
    sponsors = {
        1: 1000000,
        3: 500000,
        5: 100000,
        7: 50000
    }
    expenses = 200000

    def find_the_sponsors_amount(self, race_pos):
        amount = 0
        if race_pos == 1:
            amount += (MercedesTeam.sponsors[race_pos] + MercedesTeam.sponsors[5])
        elif 2 == race_pos or race_pos == 3:
            amount += (MercedesTeam.sponsors[3] + MercedesTeam.sponsors[5])
        elif 3 < race_pos <= 5:
            amount += MercedesTeam.sponsors[5]
        elif 5 < race_pos <= 7:
            amount += MercedesTeam.sponsors[7]
        return amount

    def calculate_revenue_after_race(self, race_pos: int):
        revenue = self.find_the_sponsors_amount(race_pos) - MercedesTeam.expenses
        self.budget += revenue
        return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"
