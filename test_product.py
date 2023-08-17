import pytest
from products import Product

def test_create_product_instance():
    '''Test that creating a normal product works.'''
    test_prod = Product("Samsung S21+", 1000, 400)
    assert isinstance(test_prod, Product)
    assert test_prod.name == "Samsung S21+"
    assert test_prod.price == 1000
    assert test_prod.quantity == 400


'''Test that creating a product with invalid details (empty name, negative price) invokes an exception:'''
def test_empty_name_raises_exception():
    with pytest.raises(ValueError, match="Invalid product details\. Product name cannot be empty\."):
        Product("", 100, 5)


def test_negative_price_raises_exception():
    with pytest.raises(ValueError, match="Invalid product details\. Product price must be positive\."):
        Product("Apple", -10, 5)


def test_negative_quantity_raises_exception():
    with pytest.raises(ValueError, match="Invalid product details\. Product quantity must be positive\."):
        Product("Samsung", 10, -5)


def test_product_becomes_inactive_at_zero_quantity():
    '''Test that when a product reaches 0 quantity, it becomes inactive.'''
    product = Product("Example", 100, 3)
    assert product.is_active()
    product.set_quantity(0)
    assert not product.is_active()  # Product should now be inactive


def test_product_purchase_modifies_quantity_and_returns_total_price():
    '''Test that product purchase modifies the quantity and returns the right output.'''
    product = Product("Example", 10, 5)

    purchased_quantity = 3
    total_price = product.buy(purchased_quantity)

    assert product.get_quantity() == 2  # 5 - 3 = 2
    assert total_price == 30.00  # Total price should be 3 * 10 = 30
    assert product.is_active()  # Product should still be active after purchase


def test_buying_larger_quantity_than_exists_raises_exception():
    '''Test that buying a larger quantity than exists invokes exception.'''
    product = Product("Example", 10, 5)
    with pytest.raises(ValueError, match="Not enough quantity available to buy\."):
        purchased_quantity = 6 #Product quantity is 5, trying to purchase 6
        product.buy(purchased_quantity)


