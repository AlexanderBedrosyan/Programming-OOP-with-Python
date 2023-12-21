from project.car.car import Car


class MuscleCar(Car):

    def speed_limit_range(self):
        return [250, 450]