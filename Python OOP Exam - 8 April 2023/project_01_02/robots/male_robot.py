from project.robots.base_robot import BaseRobot


class MaleRobot(BaseRobot):

    def __init__(self, name, kind, price):
        super().__init__(name, kind, price, 9)

    def eating(self):
        self.weight += 3