from project.booths.booth import Booth


class PrivateBooth(Booth):
    PRICE_PER_PERSON = 3.50

    def reserve(self, number_of_people: int):
        self.price_for_reservation = number_of_people * PrivateBooth.PRICE_PER_PERSON
        self.is_reserved = True