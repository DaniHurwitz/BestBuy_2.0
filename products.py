class Product:
    '''The Product class represents a specific type of product available in the store.
        It encapsulates information about the product, including its name and price and quantity of items currently
        available in the store.'''
    def __init__(self, name, price, quantity):
        try:
            if not name:
                raise ValueError("Product name cannot be empty.")
            if price < 0:
                raise ValueError("Product price must be positive.")
            if quantity < 0:
                raise ValueError("Product quantity must be positive.")
        except ValueError as e:
            raise ValueError("Invalid product details. " + str(e))

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True


    def get_quantity(self) -> int:
        return self.quantity


    def set_quantity(self, quantity):
        self.quantity = quantity
        if self.quantity == 0 and not isinstance(self, NonStockedProduct): #NonStockedProduct quantity = 0 but is active
            self.deactivate()


    def is_active(self) -> bool:
        return self.active


    def activate(self):
        self.active = True


    def deactivate(self):
        self.active = False


    def show(self) -> str:
        return f"{self.name}, Price: ${self.price}, Quantity: {self.quantity}"


    def buy(self, quantity) -> float:
        if quantity <= 0:
            raise ValueError("Invalid quantity. It must be greater than zero.")
        if quantity > self.quantity:
            raise ValueError("Not enough quantity available to buy.")

        total_price_float = float(self.price * quantity)
        self.quantity -= quantity   #remove bought products from product quantity in stock

        if self.quantity == 0:  #Out of Stock
            self.deactivate()

        return total_price_float


class NonStockedProduct(Product):
    '''The NonStockedProduct class represents a product that is not physically stocked in the store.
        It inherits from the Product class and sets the quantity to zero (unlimited).'''
    def __init__(self, name, price):
        super().__init__(name, price, 0)

    def show(self) -> str:
        return f"{self.name}, Price: ${self.price}, Quantity: Unlimited"

    def buy(self, quantity): #override buy from Product to allow purchase despite quantity = 0
        if quantity <= 0:
            raise ValueError("Invalid quantity. It must be greater than zero.")

        total_price_float = float(self.price * quantity)
        return total_price_float


class LimitedProduct(Product):
    '''The LimitedProduct class represents a product that can only be purchased a limited number of times in an order.
        It inherits from the Product class and adds a limit attribute.'''
    def __init__(self, name, price, quantity, maximum):
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def show(self) -> str:
        return f"{self.name}, Price: ${self.price}, Limited to {self.maximum} per order!"

    def buy(self, quantity): #override parent buy method to check maximum order not exceeded
        try:
            if quantity <= 0:
                raise ValueError("Invalid quantity. It must be greater than zero.")
            if quantity > self.quantity:
                raise ValueError("Not enough quantity available to buy.")
            if quantity > self.maximum:
                raise ValueError(f"Invalid quantity. Purchase of this item is limited to {self.maximum} per order.")

            total_price_float = float(self.price * quantity)
            self.quantity -= quantity

            if self.quantity == 0:  # Out of Stock
                self.deactivate()

            return total_price_float

        except ValueError as e:
            print("Error while making the purchase:", e)




