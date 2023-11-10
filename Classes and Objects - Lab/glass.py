class Glass:
    capacity = 250

    def __init__(self):
        self.content = 0

    def capacity_checker(self, result):
        return self.capacity >= result

    def fill(self, ml) -> str:
        result = ml + self.content
        if self.capacity_checker(result):
            self.content = result
            return f"Glass filled with {ml} ml"
        return f"Cannot add {ml} ml"

    def empty(self) -> str:
        self.content = 0
        return "Glass is now empty"

    def info(self) -> str:
        return f"{self.capacity - self.content} ml left"


glass = Glass()
print(glass.fill(100))
print(glass.fill(200))
print(glass.empty())
print(glass.fill(200))
print(glass.info())
