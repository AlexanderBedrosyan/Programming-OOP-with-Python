class Vet:
    animals = []
    space = 5

    def __init__(self, name: str):
        self.name = name
        self.animals = []

    def free_space_checker(self):
        return len(Vet.animals) < Vet.space

    def register_animal(self, animal_name) -> str:
        if self.free_space_checker():
            self.animals.append(animal_name)
            Vet.animals.append(animal_name)
            return f"{animal_name} registered in the clinic"
        return "Not enough space"

    def unregister_animal(self, animal_name) -> str:
        try:
            self.animals.remove(animal_name)
            Vet.animals.remove(animal_name)
            return f"{animal_name} unregistered successfully"
        except ValueError:
            return f"{animal_name} not in the clinic"

    def info(self) -> str:
        return f"{self.name} has {len(self.animals)} animals. {Vet.space - len(Vet.animals)} space left in clinic"

