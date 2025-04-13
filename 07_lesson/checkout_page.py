from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.first_name = (By.ID, "first-name")
        self.last_name = (By.ID, "last-name")
        self.postal_code = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.total_price = (By.CLASS_NAME, "summary_total_label")

    def fill_customer_info(self, first, last, zip_code):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.first_name)
        ).send_keys(first)

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.last_name)
        ).send_keys(last)

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.postal_code)
        ).send_keys(zip_code)

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.continue_button)
        ).click()

    def get_total(self):
        total_price_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.total_price)
        )
        return total_price_element.text
