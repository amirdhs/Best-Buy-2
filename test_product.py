import pytest
import Products


def test_create_product():
    # Create a product instance
    product = Products.Product("MacBook Air M2", price=1450, quantity=100)

    # Assert that the product attributes are set correctly
    assert product.name == "MacBook Air M2"
    assert product.price == 1450
    assert product.quantity == 100


def test_create_product_with_empty_name():
    # Test that creating a product with an empty name raises a ValueError
    with pytest.raises(ValueError) as exc_info:
        Products.Product("", price=1450, quantity=100)
    assert str(exc_info.value) == "Name cannot be empty."


def test_create_product_with_negative_price():
    # Test that creating a product with a negative price raises a ValueError
    with pytest.raises(ValueError) as exc_info:
        Products.Product("MacBook Air M2", price=-1450, quantity=100)
    assert str(exc_info.value) == "Price cannot be negative."


def test_product_becomes_inactive_at_zero_quantity():
    # Create a product with initial quantity > 0
    product = Products.Product("MacBook Air M2", price=1450, quantity=1)

    # Buy all available quantity
    product.buy(1)

    # Assert that the quantity is now 0 and the product is inactive
    assert product.quantity == 0


def test_product_purchase_modifies_quantity():
    # Create a product with sufficient quantity
    product = Products.Product("MacBook Air M2", price=1450, quantity=100)

    # Purchase a quantity
    product.buy(10)

    # Assert that the quantity has been reduced
    assert product.quantity == 90


def test_buy_larger_quantity_raises_exception():
    # Create a product with limited quantity
    product = Products.Product("MacBook Air M2", price=1450, quantity=10)

    # Test that buying more than available raises a ValueError
    with pytest.raises(ValueError) as exc_info:
        product.buy(20)
    assert str(exc_info.value) == "Cannot purchase 20 units; only 10 units are available."
