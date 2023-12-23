from project.player import Player
from project.supply.drink import Drink
from project.supply.food import Food
from project.supply.supply import Supply


class Controller:

    def __init__(self):
        self.players: list = []
        self.supplies: list = []

    @staticmethod
    def find_object(item: str or int, attribute: str, collection: list):
        for obj in collection:
            if getattr(obj, attribute) == item:
                return obj

    def find_supplies_by_type(self, sustenance_type):
        for obj in self.supplies[::-1]:
            if obj.__class__.__name__ == sustenance_type:
                return obj

    def add_player(self, *players):
        name_of_added_players = []
        for player in players:
            if player not in self.players:
                self.players.append(player)
                name_of_added_players.append(player.name)
        return f"Successfully added: {', '.join(name_of_added_players)}"

    def add_supply(self, *supplies):
        for supply in supplies:
            self.supplies.append(supply)

    def sustain(self, player_name: str, sustenance_type: str):
        player = self.find_object(player_name, 'name', self.players)
        if player is None:
            return

        supply = self.find_supplies_by_type(sustenance_type)

        if player.stamina == 100:
            return f"{player_name} have enough stamina."

        if sustenance_type not in ['Food', 'Drink']:
            return

        if supply is None:
            if sustenance_type == 'Food':
                raise Exception("There are no food supplies left!")
            else:
                raise Exception("There are no drink supplies left!")

        result = player.stamina + supply.energy
        if result > 100:
            player.stamina = 100
        else:
            player.stamina = result

        for i in range(len(self.supplies) - 1, - 1, - 1):
            if self.supplies[i] == supply:
                self.supplies.pop(i)
                break

        return f"{player_name} sustained successfully with {supply.name}."

    @staticmethod
    def stamina_checker(player_1, player_2):
        return [player_1, player_2] if player_1.stamina < player_2.stamina else [player_2, player_1]

    @staticmethod
    def find_the_winner(current_list) -> object:
        winner = None
        result = current_list[1].stamina - (current_list[0].stamina / 2)
        if result <= 0:
            current_list[1].stamina = 0
            winner = current_list[0]
            return winner
        current_list[1].stamina = result

        next_result = current_list[0].stamina - (current_list[1].stamina / 2)
        if next_result <= 0:
            current_list[0].stamina = 0
            winner = current_list[1]
            return winner
        current_list[0].stamina = next_result

        winner = Controller.stamina_checker(current_list[0], current_list[1])
        return winner[1]

    def duel(self, first_player_name: str, second_player_name: str):
        first_player = self.find_object(first_player_name, 'name', self.players)
        second_player = self.find_object(second_player_name, 'name', self.players)

        stamina_checker = []
        if first_player.stamina == 0:
            stamina_checker.append(f"Player {first_player_name} does not have enough stamina.")

        if second_player.stamina == 0:
            stamina_checker.append(f"Player {second_player_name} does not have enough stamina.")

        if stamina_checker:
            return '\n'.join(stamina_checker)

        duel_players = self.stamina_checker(first_player, second_player)
        return f"Winner: {self.find_the_winner(duel_players).name}"

    def next_day(self):
        for player in self.players:
            result = player.stamina - (player.age * 2)
            if result <= 0:
                player.stamina = 0
            else:
                player.stamina = result

        for player in self.players:
            self.sustain(player.name, 'Food')
            self.sustain(player.name, 'Drink')

    def __str__(self):
        result = []
        for player in self.players:
            result.append(f"Player: {player.name}, {player.age}, {player.stamina}, {player.need_sustenance}")
        for supply in self.supplies:
            result.append(f"{supply.__class__.__name__}: {supply.name}, {supply.energy}")
        return '\n'.join(result)
