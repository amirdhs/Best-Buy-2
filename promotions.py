from abc import ABC, abstractmethod


# Abstract Promotion Class
class Promotion(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity):
        pass


# Second Item at Half Price Promotion
class SecondHalfPrice(Promotion):
    def apply_promotion(self, product, quantity):
        pairs = quantity // 2
        remaining = quantity % 2
        return (pairs * 1.5 * product.price) + (remaining * product.price)


# Buy 2, Get 1 Free Promotion
class ThirdOneFree(Promotion):
    def apply_promotion(self, product, quantity):
        groups_of_three = quantity // 3
        remaining = quantity % 3
        return (groups_of_three * 2 * product.price) + (remaining * product.price)


# Percentage Discount Promotion
class PercentDiscount(Promotion):
    def __init__(self, name, percent):
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, product, quantity):
        discount = self.percent / 100
        return quantity * product.price * (1 - discount)

