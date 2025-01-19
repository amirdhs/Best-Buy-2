import promotions


# Updated Product Class
class Product:
    def __init__(self, name: str, price: float, quantity: int):
        if len(name) == 0:
            raise ValueError("Name cannot be empty.")
        if price < 0:
            raise ValueError("Price cannot be negative.")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True
        self.promotion = None

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, quantity):
        self.quantity = quantity
        print(f"Quantity of {self.name} was changed to {self.quantity}.")
        if self.quantity == 0:
            self.active = False
            print(f"{self.name} is deactivated.")

    def is_active(self):
        return self.active

    def activate(self):
        self.active = True
        print(f"{self.name} is activated.")

    def deactivate(self):
        self.active = False
        print(f"{self.name} is deactivated.")

    def show(self):
        if self.promotion:
            promo_name = self.promotion.name
        else:
            promo_name = "No promotion"

        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}, Promotion: {promo_name}")

    def set_promotion(self, promotion):
        self.promotion = promotion
        # print(f"Promotion '{promotion.name}' applied to {self.name}.")

    def buy(self, quantity):
        if quantity > self.quantity:
            raise ValueError(f"Cannot purchase {quantity} units; only {self.quantity} units are available.")

        self.quantity -= quantity

        if self.promotion:
            total_price = self.promotion.apply_promotion(self, quantity)
            promotion_name = self.promotion.name
        else:
            total_price = quantity * self.price
            promotion_name = "No promotion"

        if self.quantity == 0:
            self.active = False

        return f"Total price for {quantity} units of {self.name} with ({promotion_name}): {total_price}"


# NonStockedProduct Class
class NonStockedProduct(Product):
    def __init__(self, name, price):
        super().__init__(name, price, quantity=0)
        self.quantity = None

    def show(self):
        promo_name = self.promotion.name if self.promotion else "No promotion"
        print(f"{self.name}, Price: {self.price}, Promotion: {promo_name}")

    def buy(self, quantity):
        # No quantity for NonStockedProduct, so we just apply promotion and return price
        if self.promotion:
            total_price = self.promotion.apply_promotion(self, quantity)
        else:
            total_price = quantity * self.price

        return f"Total price for {quantity} units of {self.name}: {total_price}"

# LimitedProduct Class
class LimitedProduct(Product):
    def __init__(self, name, price, quantity, maximum):
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def show(self):
        promo_name = self.promotion.name if self.promotion else "No promotion"
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}, Maximum: {self.maximum}, Promotion: {promo_name}")

    def buy(self, quantity):
        # Check if enough stock is available for purchase
        if quantity > self.maximum:
            raise ValueError(f"Cannot purchase more than {self.maximum} units at a time.")

        # If there's a promotion, apply it
        if self.promotion:
            total_price = self.promotion.apply_promotion(self, quantity)
        else:
            total_price = quantity * self.price

        # Decrease stock based on the purchase
        self.set_quantity(self.quantity - quantity)

        return f"Total price for {quantity} units of {self.name}: {total_price}"

#
# setup initial stock of inventory
# product_list = [ Product("MacBook Air M2", price=1450, quantity=100),
#                 Product("Bose QuietComfort Earbuds", price=250, quantity=500),
#                 Product("Google Pixel 7", price=500, quantity=250),
#                 NonStockedProduct("Windows License", price=125),
#                 LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
#                ]

# # # Create promotion catalog
# second_half_price = promotions.SecondHalfPrice("Second Half price!")
# third_one_free = promotions.ThirdOneFree("Third One Free!")
# thirty_percent = promotions.PercentDiscount("30% off!", percent=30)
# #
# # # Add promotions to products
# # product_list[0].set_promotion(second_half_price)
# product_list[1].set_promotion(third_one_free)
# # product_list[3].set_promotion(thirty_percent)
# # product_list[4].set_promotion(second_half_price)
# #
# # print(product_list[0].buy(20))
# print(product_list[1].buy(30))
# # print(product_list[3].buy(20))
# # print(product_list[4].buy(10))
# # print(product_list[4].buy(9))
# print(product_list[0].buy(87))