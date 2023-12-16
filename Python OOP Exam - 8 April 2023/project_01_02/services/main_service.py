from project.services.base_service import BaseService


class MainService(BaseService):

    def __init__(self, name):
        super().__init__(name, 30)

    def details(self):
        current_robots = [str(ch.name) for ch in self.robots]
        result = [
            f"{self.name} Main Service:",
            f"Robots: {' '.join(current_robots) if len(current_robots) > 0 else 'none'}"
        ]
        return '\n'.join(result)
