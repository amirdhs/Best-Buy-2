class Product:
    def __init__(self,name: str ,price:float ,quantity:int):
        """
        Raises exceptions for invalid input.
        """
        if len(name) == 0:
            raise ValueError("Name cannot be empty.")
        if price < 0 :
            raise ValueError("Price cannot be negative.")
        if quantity < 0 :
            raise ValueError("Quantity cannot be negative.")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self):
        return self.quantity

    def set_quantity(self,quantity):
        self.quantity = quantity
        print(f"Quantity of {self.name} was changed to {self.quantity}.")
        if self.quantity == 0 :
            self.active = False
            print(f"{self.name} is deactivated.")

    def is_active(self):
        if self.active :
            return True
        else:
            return False

    def activate(self):
        self.active = True
        print(f"{self.name} is Activate.")

    def deactivate(self):
        self.active = False
        print(f"{self.name} now is Deactivate.")

    def show(self):
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")


    def buy(self, quantity):
        if not self.active:
            raise ValueError(f"{self.name} is inactive and cannot be purchased.")
        if quantity > self.quantity:
            raise ValueError(f"Cannot purchase {quantity} units; only {self.quantity} units are available.")
        self.quantity -= quantity
        if self.quantity == 0:
            self.deactivate()
        return f"Total price is: {quantity * self.price}"

class NonStockedProduct(Product):
    def __init__(self, name, price):
        super().__init__(name, price, quantity=0)
        self.quantity = None

    def show(self):
        print(f"{self.name}, Price: {self.price}")

    def buy(self, quantity):
        if quantity <= 0:
            raise ValueError("Quantity must be greater than 0.")
        total_price = quantity * self.price
        return f"Total price for {quantity} units of {self.name}: {total_price}"


class LimitedProduct(Product):
    def __init__(self, name, price, quantity, maximum):
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def show(self):
        print(f"{self.name}, Price: {self.price}, Maximum: {self.maximum}")

    def buy(self, quantity):
        if quantity > self.maximum:
            raise ValueError(f"Cannot purchase more than {self.maximum} units at a time.")
        return super().buy(quantity)
        


bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
mac = Product("MacBook Air M2", price=1450, quantity=100)
windows = NonStockedProduct("Windows License", price=125)
shipping = LimitedProduct("Shipping", price=10, quantity=250, maximum=3)

print(shipping.buy(3))
print(windows.buy(3))