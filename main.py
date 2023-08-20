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
    for index, product in enumerate(products, start=1):
        print(f"{index}. {product.show()}")
    print('--------------------------------------------------------')


def show_total_amount_in_store(store_obj): #shows available stock
    total_amount = store_obj.get_total_quantity()
    print('--------------------------------')
    print(f"Total of {total_amount} items in store")


def make_an_order(store_obj, product_list):
    list_all_products_in_store(store_obj)

    shopping_list = []  # create shopping_list of tuples to use in store_obj.order(shopping_list) from store.py
    print("When you want to finish order, enter empty text.")
    while True:
        selected_product = input("Enter product number you want to order: ")
        if selected_product == '':
            break
        selected_quantity = input("Enter the quantity you want to order: ")

        try:
            product = product_list[int(selected_product) - 1]
            quantity = int(selected_quantity)

            if quantity <= 0:
                print("Error: Invalid quantity. It must be greater than zero.")
                continue  # Prompt for input again

            if isinstance(product, products.NonStockedProduct): #allow purchase on NonStocked (unlimited quantity = 0)
                shopping_list.append((product, quantity))
                print(f"Product added to list! {product.name}, quantity: {quantity}")

            elif isinstance(product, products.LimitedProduct) and quantity > product.maximum:
                print(f"Error: Invalid quantity. Purchase of {product.name} is limited to {product.maximum} per order.")
                continue

            elif quantity > product.quantity:
                print(f"Error: Not enough quantity available for product: {product.name}")
                continue

            else: #normal product order
                shopping_list.append((product, quantity))
                print(f"Product added to list! {product.name}, quantity: {quantity}")

        except (ValueError, IndexError) as e:
            print(f"Error: {e}. Please try again.")

    order_total = store_obj.order(shopping_list)
    order_total = "{:.2f}".format(order_total)
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
        # setup initial stock of inventory
        product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                        products.Product("Google Pixel 7", price=500, quantity=250),
                        products.NonStockedProduct("Windows License", price=125),
                        products.LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
                        ]
    except ValueError as e:
        print(f"Error while creating product: {e}")
        return

    best_buy = store.Store(product_list)

    start(best_buy, product_list)

if __name__ == "__main__":
    main()
