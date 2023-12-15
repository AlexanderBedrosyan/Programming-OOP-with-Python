from typing import List

from project.band import Band
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.singer import Singer
from project.concert import Concert
from project import helper


class ConcertTrackerApp:

    def __init__(self):
        self.bands: List[Band] = []
        self.musicians: List[Drummer, Guitarist, Singer] = []
        self.concerts: List[Concert] = []

    @staticmethod
    def __musicians_type_validator(current_musician):
        musician_types = {
            "Guitarist": Guitarist,
            "Drummer": Drummer,
            "Singer": Singer
        }
        if current_musician in musician_types:
            return musician_types[current_musician]

    def create_musician(self, musician_type: str, name: str, age: int):
        if self.__musicians_type_validator(musician_type) is None:
            raise ValueError("Invalid musician type!")

        if helper.find_object(name, 'name', self.musicians) is not None:
            raise Exception(f"{name} is already a musician!")

        new_musician = self.__musicians_type_validator(musician_type)(name, age)
        self.musicians.append(new_musician)
        return f"{name} is now a {musician_type}."

    def create_band(self, name: str):
        if helper.find_object(name, 'name', self.bands) is not None:
            raise Exception(f"{name} band is already created!")

        new_band = Band(name)
        self.bands.append(new_band)
        return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        concert_exist = helper.find_object(place, 'place', self.concerts)
        if concert_exist is not None:
            raise Exception(f"{place} is already registered for {concert_exist.genre} concert!")

        new_concert = Concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(new_concert)
        return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str):
        musician = helper.find_object(musician_name, 'name', self.musicians)
        if musician is None:
            raise Exception(f"{musician_name} isn't a musician!")

        band = helper.find_object(band_name, 'name', self.bands)
        if band is None:
            raise Exception(f"{band_name} isn't a band!")

        band.members.append(musician)
        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        band = helper.find_object(band_name, 'name', self.bands)
        if band is None:
            raise Exception(f"{band_name} isn't a band!")

        musician = helper.find_object(musician_name, 'name', band.members)
        if musician is None:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")

        band.members.remove(musician)
        return f"{musician_name} was removed from {band_name}."

    @staticmethod
    def is_concert_start(type_of_concert, band):
        drummer = [musician for musician in band.members if musician.__class__.__name__ == 'Drummer'][0]
        singer = [musician for musician in band.members if musician.__class__.__name__ == 'Singer'][0]
        guitarist = [musician for musician in band.members if musician.__class__.__name__ == 'Guitarist'][0]
        if type_of_concert == 'Rock':
            return 'play the drums with drumsticks' in drummer.skills and \
                    'sing high pitch notes' in singer.skills and \
                    'play rock' in guitarist.skills

        elif type_of_concert == 'Metal':
            return 'play the drums with drumsticks' in drummer.skills and \
                'sing low pitch notes' in singer.skills and \
                'play metal' in guitarist.skills

        else:
            return 'play the drums with drum brushes' in drummer.skills and \
                'sing low pitch notes' in singer.skills and \
                'play jazz' in guitarist.skills and 'sing high pitch notes' in singer.skills

    def start_concert(self, concert_place: str, band_name: str):
        concert = helper.find_object(concert_place, 'place', self.concerts)
        band = helper.find_object(band_name, 'name', self.bands)

        list_of_member_types = [musician.__class__.__name__ for musician in band.members]
        needed_list_of_musicians = ["Guitarist", "Drummer", "Singer"]
        if not all(element in list_of_member_types for element in needed_list_of_musicians):
            raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")

        if not self.is_concert_start(concert.genre, band):
            raise Exception(f"The {band_name} band is not ready to play at the concert!")

        profit = (concert.audience * concert.ticket_price) - concert.expenses
        return f"{band_name} gained {profit:.2f}$ from the {concert.genre} concert in {concert_place}."


