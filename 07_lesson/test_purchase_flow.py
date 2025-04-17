import sys
import os
import pytest
from selenium import webdriver
from login_page import LoginPage
from inventory_page import InventoryPage
from cart_page import CartPage
from checkout_page import CheckoutPage

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "../pages"
        )
    )
)


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_purchase_total(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(driver)
    inventory_page.add_to_cart("Sauce Labs Backpack")
    inventory_page.add_to_cart("Sauce Labs Bolt T-Shirt")
    inventory_page.add_to_cart("Sauce Labs Onesie")
    inventory_page.go_to_cart()

    cart_page = CartPage(driver)
    cart_page.proceed_to_checkout()

    checkout_page = CheckoutPage(driver)
    checkout_page.fill_customer_info("Alex", "Kartaguzov", "123456")
    total = checkout_page.get_total()

    assert total == "Total: $58.29", f"Expected $58.29, but got {total}"
