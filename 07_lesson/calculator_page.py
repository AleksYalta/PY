from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = (
            "https://bonigarcia.dev/selenium-webdriver-java/"
            "slow-calculator.html"
        )
        self.delay_input = (By.ID, "delay")
        self.result_output = (By.CSS_SELECTOR, ".screen")

    def button_locator(self, value):
        return By.XPATH, f"//span[text()='{value}']"

    def open(self):
        self.driver.get(self.url)

    def set_delay(self, seconds):
        delay_elem = self.driver.find_element(*self.delay_input)
        delay_elem.clear()
        delay_elem.send_keys(str(seconds))

    def click_button(self, value):
        button = self.driver.find_element(*self.button_locator(value))
        button.click()

    def get_result(self, expected_result="15", timeout=45):
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element
            (self.result_output, expected_result)
        )
        return self.driver.find_element(*self.result_output).text
