from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.cart_button = (By.CLASS_NAME, "shopping_cart_link")

    def add_to_cart(self, product_name):
        locator = (
            By.XPATH,
            f"//div[text()='{product_name}']"
            "/ancestor::div[@class='inventory_item']//button"
        )

        add_to_cart_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        )
        add_to_cart_button.click()

    def go_to_cart(self):
        cart_button_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.cart_button)
        )
        cart_button_element.click()
