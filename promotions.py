from abc import ABC, abstractmethod


class Promotion(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity):
        pass


class PercentDiscount(Promotion):
    '''Get a disocunt of X% where X = percent param'''
    def __init__(self, name, percent):
        super().__init__(name)
        self.percentage = percent

    def apply_promotion(self, product, quantity):
        if quantity <= 0:
            raise ValueError("Invalid quantity. It must be greater than zero.")

        original_price = product.price * quantity
        discount_amount = (self.percentage / 100) * original_price
        discounted_price = original_price - discount_amount

        return discounted_price


class SecondHalfPrice(Promotion):
    '''Second item at half price - for every two items bought, get one free.'''
    def __init__(self, name):
        super().__init__(name)

    def apply_promotion(self, product, quantity):
        half_price_items = quantity // 2  # Calculate how many items are eligible for half price
        full_price_items = quantity - half_price_items  # Calculate the remaining items at full price
        promotion_price = (half_price_items * product.price * 0.5) + (full_price_items * product.price)

        return promotion_price


class ThirdOneFree(Promotion):
    '''Buy 2, get 1 free - for every 3 items bought, 1 item is free'''
    def __init__(self, name):
        super().__init__(name)

    def apply_promotion(self, product, quantity):
        free_items = quantity // 3  # Calculate the number of items that will be free
        total_cost = (quantity - free_items) * product_price

        return total_cost
