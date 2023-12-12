from project.booths.booth import Booth


class OpenBooth(Booth):
    PRICE_PER_PERSON = 2.50

    def reserve(self, number_of_people:int):
        self.price_for_reservation = number_of_people * OpenBooth.PRICE_PER_PERSON
        self.is_reserved = True