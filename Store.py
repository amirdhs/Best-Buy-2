import Products

class Store:
    def __init__(self,products):
        if products:
            self.products = products
        else:
            self.products = []

    def add_product(self,product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)

    def get_total_quantity(self):
        total_quantity = 0
        for product in self.products:
            if product.quantity is not None:  # Check if quantity is valid
                total_quantity += product.quantity

        return f"{total_quantity} items are in the store in total."

    def get_all_products(self):
        active_products = []
        for product in self.products:
            if product.is_active():
                active_products.append(product)
        return active_products

    def order(self, shopping_list):
        total_price = 0
        for product, quantity in shopping_list:
            if not product.is_active():
                raise ValueError(f"Cannot order {product.name}, as it is inactive.")
            if quantity > product.quantity:
                raise ValueError(f"Cannot order {quantity} units of {product.name}; only {product.quantity} available.")
            total_price += product.price * quantity
            product.buy(quantity)
            if product.quantity == 0 :
                product.deactivate()
        return f"{total_price} dollars"

#
# bose = Products.Product("Bose QuietComfort Earbuds", price=250, quantity=500)
# mac = Products.Product("MacBook Air M2", price=1450, quantity=100)
#
# store = Store([bose, mac])
#
# pixel = Products.Product("Google Pixel 7", price=500, quantity=250)
# store.add_product(pixel)
#
# product_list = [Products.Product("MacBook Air M2", price=1450, quantity=100),
#                  Products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
#                  Products.Product("Google Pixel 7", price=500, quantity=250),
#                 ]
# #
# store = Store(product_list)
# products = store.get_all_products()
# print(store.get_total_quantity())
# print(store.order([(products[0], 1), (products[1], 2)]))

