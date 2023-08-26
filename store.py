from products import NonStockedProduct, LimitedProduct


class Store():
    '''Holds all instances of products, and will allow the user to make a purchase of multiple products at once.'''
    def __init__(self, products=None): #set default if not provided
        if products is None:
            self.list_of_products = [] #if store is initially empty
        else:
            self.list_of_products = products


    def add_product(self, product):
        self.list_of_products.append(product)


    def remove_product(self, product_name):
        for product in self.list_of_products:
            if product.name == product_name:    #Remove product that matches the name of the product provided in param
                self.list_of_products.remove(product)
                break


    def get_total_quantity(self) -> int:
        '''Returns how many items are in the store in total.'''
        total = 0
        for product in self.list_of_products:
            total += product.quantity
        return total


    def get_all_products(self):
        '''Returns all products in the store that are active.'''
        active_products = []
        for product in self.list_of_products:
            if product.is_active():
                active_products.append(product)
        return active_products


    def order(self, shopping_list) -> float:
        '''Gets a list of tuples, where each tuple has 2 items: Product (Product class) and quantity (int).
        Buys the products and returns the total price of the order.'''
        total_cost = 0

        for product_obj, quantity in shopping_list:
            if quantity <= 0:
                raise ValueError("Invalid quantity. It must be greater than zero.")

            if isinstance(product_obj, NonStockedProduct): #allow purchase despite quantity=0
                total_cost += product_obj.buy(quantity)
            else:
                available_quantity = product_obj.get_quantity()
                if available_quantity >= quantity:
                    total_cost += product_obj.buy(quantity)
                else:
                    raise ValueError(
                        f"Not enough quantity available for product: {product_obj.name}")
        return total_cost


