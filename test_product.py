import pytest
import Products
import Store
import promotions

def test_create_product():
    product = Products.Product("MacBook Air M2", price=1450, quantity=100)
    assert product.name == "MacBook Air M2"
    assert product.price == 1450
    assert product.quantity == 100

def test_create_product_with_empty_name():
    with pytest.raises(ValueError) as exc_info:
        Products.Product("", price=1450, quantity=100)
    assert str(exc_info.value) == "Name cannot be empty."

def test_create_product_with_negative_price():
    with pytest.raises(ValueError) as exc_info:
        Products.Product("MacBook Air M2", price=-1450, quantity=100)
    assert str(exc_info.value) == "Price cannot be negative."

def test_product_becomes_inactive_at_zero_quantity():
    product = Products.Product("MacBook Air M2", price=1450, quantity=1)
    product.buy(1)
    assert product.quantity == 0
    assert not product.is_active()

def test_product_purchase_modifies_quantity():
    product = Products.Product("MacBook Air M2", price=1450, quantity=100)
    product.buy(10)
    assert product.quantity == 90

def test_buy_larger_quantity_raises_exception():
    product = Products.Product("MacBook Air M2", price=1450, quantity=10)
    with pytest.raises(ValueError) as exc_info:
        product.buy(20)
    assert str(exc_info.value) == "Cannot purchase 20 units; only 10 units are available."

def test_non_stocked_product():
    product = Products.NonStockedProduct("Windows License", price=125)
    assert product.quantity is None
    assert product.buy(1) == "Total price for 1 units of Windows License: 125"

def test_limited_product():
    product = Products.LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
    assert product.quantity == 250
    assert product.maximum == 1
    assert product.buy(1) == "Total price for 1 units of Shipping: 10"
    with pytest.raises(ValueError) as exc_info:
        product.buy(2)
    assert str(exc_info.value) == "Cannot purchase more than 1 units at a time."

def test_product_with_second_half_price_promotion():
    product = Products.Product("MacBook Air M2", price=1450, quantity=2)
    promo = promotions.SecondHalfPrice("Second Half price!")
    product.set_promotion(promo)
    assert product.buy(2) == "Total price for 2 units of MacBook Air M2 with (Second Half price!): 2175.0"

def test_product_with_third_one_free_promotion():
    product = Products.Product("MacBook Air M2", price=1450, quantity=3)
    promo = promotions.ThirdOneFree("Third One Free!")
    product.set_promotion(promo)
    assert product.buy(3) == "Total price for 3 units of MacBook Air M2 with (Third One Free!): 2900"

def test_product_with_percent_discount():
    product = Products.Product("MacBook Air M2", price=1450, quantity=3)
    promo = promotions.PercentDiscount("30% off!", percent=30)
    product.set_promotion(promo)
    assert product.buy(3) == "Total price for 3 units of MacBook Air M2 with (30% off!): 3045.0"

def test_get_total_quantity():
    product_list = [
        Products.Product("MacBook Air M2", price=1450, quantity=100),
        Products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Products.NonStockedProduct("Windows License", price=125),
        Products.LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
    ]
    store = Store.Store(product_list)
    assert store.get_total_quantity() == "850 items are in the store in total."
