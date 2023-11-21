from football_team_generator.player import Player


class Team:

    def __init__(self, name: str, rating: int):
        self.__name = name
        self.__rating = rating
        self.__players: list = []

    def find_player(self, list_of_players, current_player):
        for player in list_of_players:
            if player.name == current_player:
                return player

    def add_player(self, player: Player):
        if player in self.__players:
            return f"Player {player.name} has already joined"
        self.__players.append(player)
        return f"Player {player.name} joined team {self.__name}"

    def remove_player(self, player_name: str):
        player_found = self.find_player(self.__players, player_name)
        if player_found is None:
            return f"Player {player_name} not found"
        self.__players.remove(player_found)
        return player_found
