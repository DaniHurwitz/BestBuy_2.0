import products
import store

def print_store_menu():
    store_menu = '''
    Store Menu   
    ----------
    1. List all products in store
    2. Show total amount in store
    3. Make an order
    4. Quit
    '''
    print(store_menu)


def list_all_products_in_store(store_obj):
    products = store_obj.get_all_products()
    print('--------------------------------------------------------')
    for index, product in enumerate(products, start=1): #enumerate() takes iterable and returns pairs of index and value
        print(f"{index}. {product['name']}, Price: ${product['price']}, Quantity: {product['quantity']} ")
    print('--------------------------------------------------------')


def show_total_amount_in_store(store_obj): #shows available stock
    total_amount = store_obj.get_total_quantity()
    print('--------------------------------')
    print(f"Total of {total_amount} items in store")


def make_an_order(store_obj, product_list):
    list_all_products_in_store(store_obj)

    shopping_list = []  #create shopping_list of tuples to use in store_obj.order(shopping_list) from store.py
    print("When you want to finish order, enter empty text.")
    while True:
        selected_product = input("Enter product number you want to order: ")
        if selected_product == '':
            break
        selected_quantity = input("Enter the quantity you want to order: ")

        try:
            product = product_list[int(selected_product) - 1] #retrieving the appropriate product from the product_list
                # based on the user's selected product index (minus 1, to account for the 0-based indexing in the list)
            quantity = int(selected_quantity)
            if quantity > product.quantity:
                raise ValueError(f"Not enough quantity available for product: {product.name}")
            shopping_list.append((product, quantity))
            print(f"Product added to list! {product.name}, quantity: {quantity}")
        except (ValueError, IndexError):
            print(f"Invalid product number or quantity. Please try again.")

    order_total = store_obj.order(shopping_list)
    order_total = "{:.2f}".format(order_total) #format to 2 decimal places
    print("********")
    print(f"Order made! Total payment: ${order_total}")


def start(store_obj, product_list):
    '''Initiates the menu-driven interaction loop for managing the store'''
    while True:
        print_store_menu()
        user_selection = input("Please choose a number: ")

        if user_selection == '1':
            list_all_products_in_store(store_obj)
        elif user_selection == '2':
            show_total_amount_in_store(store_obj)
        elif user_selection == '3':
            make_an_order(store_obj,product_list)
        elif user_selection == '4':
            break
        else:
            print("Invalid input. Please choose a valid number or 'exit'.")


def main():
    try:
        product_list = [
            products.Product("MacBook Air M2", price=1450, quantity=100),
            products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
            products.Product("Google Pixel 7", price=500, quantity=250)
        ]
    except ValueError as e:
        print(f"Error while creating product: {e}")
        return

    best_buy = store.Store(product_list)

    start(best_buy, product_list)

if __name__ == "__main__":
    main()
