class Cup:

    def __init__(self, size:int, quantity:int):
        self.size = size
        self.quantity = quantity

    def fill(self, quantity):
        new_quantity = self.quantity + quantity
        if new_quantity <= self.size:
            self.quantity = new_quantity

    def status(self):
        return self.size - self.quantity
