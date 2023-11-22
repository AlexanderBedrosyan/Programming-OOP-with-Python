from wild_cat_zoo.animal import Animal
from wild_cat_zoo.worker import Worker


class Zoo:

    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals: list = []
        self.workers: list = []

    def find_object(self, item: str or int, attribute: str, collection: list):
        for obj in collection:
            if getattr(obj, attribute) == item:
                return obj

    def add_animal(self, animal, price):
        if self.__budget < price:
            return "Not enough budget"
        if len(self.animals) >= self.__animal_capacity:
            return "Not enough space for animal"
        self.__budget -= price
        self.animals.append(animal)
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker):
        if len(self.workers) >= self.__workers_capacity:
            return "Not enough space for worker"
        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name):
        find_object_of_current_worker = self.find_object(worker_name, "name", self.workers)
        if find_object_of_current_worker is None:
            return f"There is no {worker_name} in the zoo"
        self.workers.remove(find_object_of_current_worker)
        return f"{worker_name} fired successfully"

    def pay_workers(self):
        needed_money_for_salary = 0
        for current_worker in self.workers:
            needed_money_for_salary += current_worker.salary
        if self.__budget >= needed_money_for_salary:
            self.__budget -= needed_money_for_salary
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        needed_money_for_animal_care = 0
        for current_animal in self.animals:
            needed_money_for_animal_care += current_animal.money_for_care
        if self.__budget >= needed_money_for_animal_care:
            self.__budget -= needed_money_for_animal_care
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = [f"You have {len(self.animals)} animals"]
        lions = [current_animal.__repr__() for current_animal in self.animals
                 if current_animal.__class__.__name__ == "Lion"]
        tigers = [current_animal.__repr__() for current_animal in self.animals
                  if current_animal.__class__.__name__ == "Tiger"]
        cheetahs = [current_animal.__repr__() for current_animal in self.animals
                    if current_animal.__class__.__name__ == "Cheetah"]
        result.append(f"----- {len(lions)} Lions:")
        [result.append(lion) for lion in lions]
        result.append(f"----- {len(tigers)} Tigers:")
        [result.append(tiger) for tiger in tigers]
        result.append(f"----- {len(tigers)} Cheetahs:")
        [result.append(cheetah) for cheetah in cheetahs]
        return '\n'.join(result)

    def workers_status(self):
        result = [f"You have {len(self.workers)} workers"]
        keepers = [current_worker.__repr__() for current_worker in self.workers if
                 current_worker.__class__.__name__ == "Keeper"]
        caretakers = [current_worker.__repr__() for current_worker in self.workers if
                 current_worker.__class__.__name__ == "Caretaker"]
        vets = [current_worker.__repr__() for current_worker in self.workers if
                 current_worker.__class__.__name__ == "Vet"]
        result.append(f"----- {len(keepers)} Keepers:")
        [result.append(keeper) for keeper in keepers]
        result.append(f"----- {len(caretakers)} Caretakers:")
        [result.append(caretaker) for caretaker in caretakers]
        result.append(f"----- {len(vets)} Vets:")
        [result.append(vet) for vet in vets]
        return '\n'.join(result)
