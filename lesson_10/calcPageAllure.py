import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver

class CalculatorPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        self.delay_input = (By.ID, "delay")
        self.result_output = (By.CSS_SELECTOR, ".screen")

    def button_locator(self, value: str) -> tuple:
        return By.XPATH, f"//span[text()='{value}']"

    @allure.step("Открываем страницу калькулятора")
    def open(self) -> None:
        self.driver.get(self.url)

    @allure.step("Устанавливаем задержку: {seconds} сек.")
    def set_delay(self, seconds: int) -> None:
        delay_elem = self.driver.find_element(*self.delay_input)
        delay_elem.clear()
        delay_elem.send_keys(str(seconds))

    @allure.step("Нажимаем кнопку: {value}")
    def click_button(self, value: str) -> None:
        button = self.driver.find_element(*self.button_locator(value))
        button.click()

    @allure.step("Получаем результат")
    def get_result(self, expected_result: str = "15", timeout: int = 60) -> str:
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(self.result_output, expected_result)
        )
        return self.driver.find_element(*self.result_output).text
