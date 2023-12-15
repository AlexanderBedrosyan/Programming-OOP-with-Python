from project.horse_specification.horse import Horse


class Thoroughbred(Horse):

    def increase_speed(self):
        return 3

    def maximum_speed(self):
        return 140