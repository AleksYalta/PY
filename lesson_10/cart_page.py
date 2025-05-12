import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class CartPage:
    def __init__(self, driver: WebDriver):
        """
        Инициализирует страницу корзины.

        :param driver: Экземпляр Selenium WebDriver
        """
        self.driver = driver
        self.checkout_button = (By.ID, "checkout")

    @allure.step("Переход к оформлению заказа (Checkout)")
    def proceed_to_checkout(self) -> None:
        """
        Кликает по кнопке 'Checkout' и переходит к оформлению заказа.

        :return: None
        """
        checkout_button_element = WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable(self.checkout_button)
        )
        checkout_button_element.click()
