from project.car.car import Car


class SportsCar(Car):

    def speed_limit_range(self):
        return [400, 600]
