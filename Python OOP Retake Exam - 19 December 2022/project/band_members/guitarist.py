from project.band_members.musician import Musician


class Guitarist(Musician):

    def available_skills(self):
        return ["play metal", "play rock", "play jazz"]
