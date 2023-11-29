from project.formula_teams.formula_team import FormulaTeam


class RedBullTeam(FormulaTeam):
    sponsors = {
        1: 1500000,
        2: 800000,
        8: 20000,
        10: 10000
    }
    expenses = 250000

    def find_the_sponsors_amount(self, race_pos):
        amount = 0
        if race_pos == 1 or race_pos == 2:
            amount += (RedBullTeam.sponsors[race_pos] + RedBullTeam.sponsors[8])
        elif 2 < race_pos <= 8:
            amount += RedBullTeam.sponsors[8]
        elif 8 < race_pos <= 10:
            amount += RedBullTeam.sponsors[10]
        return amount

    def calculate_revenue_after_race(self, race_pos: int):
        revenue = self.find_the_sponsors_amount(race_pos) - RedBullTeam.expenses
        self.budget += revenue
        return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"