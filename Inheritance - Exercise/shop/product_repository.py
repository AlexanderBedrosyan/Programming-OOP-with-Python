from project.product import Product


class ProductRepository:

    def __init__(self):
        self.products: list = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str):
        product = [prd for prd in self.products if prd.name == product_name]
        if len(product) > 0:
            return product[0]

    def remove(self, product_name):
        index = None
        for i in range(len(self.products)):
            if self.products[i].name == product_name:
                index = i
        if index is not None:
            self.products.pop(index)

    def __repr__(self):
        result = []
        for prd in self.products:
            result.append(f"{prd.name}: {prd.quantity}")
        return '\n'.join(result)