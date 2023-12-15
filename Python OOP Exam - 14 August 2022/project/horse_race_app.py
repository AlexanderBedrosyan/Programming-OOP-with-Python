from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey


class HorseRaceApp:

    def __init__(self):
        self.horses: list = []
        self.jockeys: list = []
        self.horse_races: list = []

    @staticmethod
    def find_object(item: str or int, attribute: str, collection: list):
        for obj in collection:
            if getattr(obj, attribute) == item:
                return obj

    @staticmethod
    def valid_horses(horse_type):
        horses = {
            "Appaloosa": Appaloosa,
            "Thoroughbred": Thoroughbred
        }
        if horse_type in horses:
            return horses[horse_type]

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        if self.find_object(horse_name, 'name', self.horses) is not None:
            raise Exception(f"Horse {horse_name} has been already added!")
        if self.valid_horses(horse_type) is None:
            return

        new_horse = self.valid_horses(horse_type)(horse_name, horse_speed)
        self.horses.append(new_horse)
        return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        if self.find_object(jockey_name, 'name', self.jockeys) is not None:
            raise Exception(f"Jockey {jockey_name} has been already added!")

        new_jockey = Jockey(jockey_name, age)
        self.jockeys.append(new_jockey)
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        if self.find_object(race_type, 'race_type', self.horse_races) is not None:
            raise Exception(f"Race {race_type} has been already created!")

        new_race = HorseRace(race_type)
        self.horse_races.append(new_race)
        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        if self.find_object(jockey_name, 'name', self.jockeys) is None:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        horses_from_exact_type = [horse for horse in self.horses if horse.__class__.__name__ == horse_type]
        needed_horse = None
        if horses_from_exact_type:
            for i in range(len(horses_from_exact_type) - 1, - 1, - 1):
                if not horses_from_exact_type[i].is_taken:
                    needed_horse = horses_from_exact_type[i]
                    break

        if needed_horse is None:
            raise Exception(f"Horse breed {horse_type} could not be found!")

        jockey = self.find_object(jockey_name, 'name', self.jockeys)

        if jockey.horse is not None:
            return f"Jockey {jockey_name} already has a horse."

        jockey.horse = needed_horse
        needed_horse.is_taken = True
        return f"Jockey {jockey_name} will ride the horse {needed_horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        horse_race = self.find_object(race_type, 'race_type', self.horse_races)

        if horse_race is None:
            raise Exception(f"Race {race_type} could not be found!")

        jockey = self.find_object(jockey_name, 'name', self.jockeys)

        if jockey is None:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        if jockey.horse is None:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")

        if jockey in horse_race.jockeys:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."

        horse_race.jockeys.append(jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        horse_race = self.find_object(race_type, 'race_type', self.horse_races)

        if horse_race is None:
            raise Exception(f"Race {race_type} could not be found!")

        if len(horse_race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        sorted_jockeys = list(sorted(horse_race.jockeys, key=lambda jockey: -jockey.horse.speed))

        return f"The winner of the {race_type} race, with a speed of {sorted_jockeys[0].horse.speed}km/h is {sorted_jockeys[0].name}! Winner's horse: {sorted_jockeys[0].horse.name}."


horseRaceApp = HorseRaceApp()
print(horseRaceApp.add_horse("Appaloosa", "Spirit", 80))
print(horseRaceApp.add_horse("Thoroughbred", "Rocket", 110))
print(horseRaceApp.add_jockey("Peter", 19))
print(horseRaceApp.add_jockey("Mariya", 21))
print(horseRaceApp.create_horse_race("Summer"))
print(horseRaceApp.add_horse_to_jockey("Peter", "Appaloosa"))
print(horseRaceApp.add_horse_to_jockey("Peter", "Thoroughbred"))
print(horseRaceApp.add_horse_to_jockey("Mariya", "Thoroughbred"))
print(horseRaceApp.add_jockey_to_horse_race("Summer", "Mariya"))
print(horseRaceApp.add_jockey_to_horse_race("Summer", "Peter"))
print(horseRaceApp.add_jockey_to_horse_race("Summer", "Mariya"))
print(horseRaceApp.start_horse_race("Summer"))

