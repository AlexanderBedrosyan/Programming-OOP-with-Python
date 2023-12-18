from project.shopping_cart import ShoppingCart
import unittest


class Test(unittest.TestCase):

    def setUp(self):
        self.my_cart = ShoppingCart('Gosho', 100)

    def test_init(self):
        self.assertEqual(self.my_cart.shop_name, 'Gosho')
        self.assertEqual(self.my_cart.budget, 100)
        self.assertEqual(self.my_cart.products, {})

    def test_shop_name_setter_if_value_error_is_raised(self):
        with self.assertRaises(ValueError) as va:
            ShoppingCart('wrong', 100)
        self.assertEqual(str(va.exception), "Shop must contain only letters and must start with capital letter!")

        with self.assertRaises(ValueError) as va:
            ShoppingCart('A12312312', 100)
        self.assertEqual(str(va.exception), "Shop must contain only letters and must start with capital letter!")

        with self.assertRaises(ValueError) as va:
            ShoppingCart('A@/', 100)
        self.assertEqual(str(va.exception), "Shop must contain only letters and must start with capital letter!")

        with self.assertRaises(ValueError) as va:
            ShoppingCart('Aasdasdda1', 100)
        self.assertEqual(str(va.exception), "Shop must contain only letters and must start with capital letter!")

        with self.assertRaises(ValueError) as va:
            self.my_cart.shop_name = 'dosadna greshka'
        self.assertEqual(str(va.exception), "Shop must contain only letters and must start with capital letter!")

        with self.assertRaises(ValueError) as va:
            self.my_cart.shop_name = 'AbraKadabra1'
        self.assertEqual(str(va.exception), "Shop must contain only letters and must start with capital letter!")

        with self.assertRaises(ValueError) as va:
            self.my_cart.shop_name = 'Abra kadabra'
        self.assertEqual(str(va.exception), "Shop must contain only letters and must start with capital letter!")

    def test_add_to_cart(self):
        with self.assertRaises(ValueError) as va:
            self.my_cart.add_to_cart('TV', 100.0)
        self.assertEqual(str(va.exception), f"Product TV cost too much!" )

        with self.assertRaises(ValueError) as va:
            self.my_cart.add_to_cart('TV', 100.1)
        self.assertEqual(str(va.exception), f"Product TV cost too much!")

        result = self.my_cart.add_to_cart('TV', 99.99)
        self.assertEqual(result, f"TV product was successfully added to the cart!")
        self.assertEqual(self.my_cart.products, {'TV': 99.99})
        self.assertEqual(len(self.my_cart.products), 1)

        result3 = self.my_cart.add_to_cart('TV', 10)
        self.assertEqual(self.my_cart.products, {'TV': 10})
        self.assertEqual(result3, f"TV product was successfully added to the cart!")

        result2 = self.my_cart.add_to_cart('Laptop', 22)
        self.assertEqual(result2, f"Laptop product was successfully added to the cart!")
        self.assertEqual(self.my_cart.products, {'TV': 10, 'Laptop': 22})
        self.assertEqual(len(self.my_cart.products), 2)

    def test_remove_from_cart(self):
        self.my_cart.add_to_cart('Book', 26)
        with self.assertRaises(ValueError) as va:
            self.my_cart.remove_from_cart('TV')
        self.assertEqual(str(va.exception), f"No product with name TV in the cart!")
        self.assertEqual(self.my_cart.products, {'Book': 26})

        self.my_cart.add_to_cart('TV', 16)
        self.my_cart.add_to_cart('Laptop', 13)
        result = self.my_cart.remove_from_cart('TV')

        self.assertEqual(result, "Product TV was successfully removed from the cart!")
        self.assertEqual(self.my_cart.products, {'Book': 26, 'Laptop': 13})
        self.assertEqual(len(self.my_cart.products), 2)

    def test_add_new_shop(self):
        second_shop = ShoppingCart('Pesho', 200)
        self.my_cart.add_to_cart('TV', 50)
        second_shop.add_to_cart('Laptop', 20)
        new_shopping_cart = self.my_cart + second_shop

        self.assertEqual(new_shopping_cart.shop_name, 'GoshoPesho')
        self.assertEqual(new_shopping_cart.budget, 300)
        self.assertEqual(new_shopping_cart.products, {'TV': 50, 'Laptop': 20})

    def test_add_new_shop_with_add(self):
        second_shop = ShoppingCart('Goshov', 200)
        self.my_cart.products = {'TV': 50, 'BALL': 70, 'BOOK': 33}
        second_shop.products = {'SMARTPHONE': 99}
        new_shop = second_shop.__add__(self.my_cart)

        self.assertEqual(new_shop.shop_name, 'GoshovGosho')
        self.assertEqual(new_shop.budget, 300)
        self.assertEqual(new_shop.products, {'SMARTPHONE': 99, 'TV': 50, 'BALL': 70, 'BOOK': 33})

    def test_add_new_shop_with_equal_products(self):
        second_shop = ShoppingCart('Pesho', 200)
        self.my_cart.add_to_cart('TV', 50)
        second_shop.add_to_cart('TV', 20)
        new_shopping_cart = self.my_cart + second_shop

        self.assertEqual(new_shopping_cart.shop_name, 'GoshoPesho')
        self.assertEqual(new_shopping_cart.budget, 300)
        self.assertEqual(new_shopping_cart.products, {'TV': 20})

    def test_buy_products(self):
        self.my_cart.add_to_cart('TV', 50)
        self.my_cart.add_to_cart('Laptop', 70)
        with self.assertRaises(ValueError) as va:
            self.my_cart.buy_products()
        self.assertEqual(str(va.exception), f"Not enough money to buy the products! Over budget with 20.00lv!")

        self.my_cart.budget = 150
        self.assertEqual(self.my_cart.budget, 150)
        result = self.my_cart.buy_products()
        self.assertEqual(result, f'Products were successfully bought! Total cost: 120.00lv.')

    def test_buy_products_if_equal_budget_and_total_price(self):
        self.my_cart.add_to_cart('TV', 99)
        self.my_cart.add_to_cart('Laptop', 1)
        result = self.my_cart.buy_products()

        self.assertEqual(result, f'Products were successfully bought! Total cost: 100.00lv.')
        self.assertEqual(self.my_cart.budget, 100)
