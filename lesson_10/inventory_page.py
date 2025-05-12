import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class InventoryPage:
    def __init__(self, driver: WebDriver):
        """
        Инициализирует страницу списка товаров.

        :param driver: Экземпляр Selenium WebDriver
        """
        self.driver = driver
        self.cart_button = (By.CLASS_NAME, "shopping_cart_link")

    @allure.step("Добавляем товар в корзину: {product_name}")
    def add_to_cart(self, product_name: str) -> None:
        """
        Находит и добавляет указанный товар в корзину по имени.

        :param product_name: Название товара, как отображается на странице
        :return: None
        """
        locator = (
            By.XPATH,
            f"//div[text()='{product_name}']"
            "/ancestor::div[@class='inventory_item']//button"
        )
        add_to_cart_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        )
        add_to_cart_button.click()

    @allure.step("Переход в корзину")
    def go_to_cart(self) -> None:
        """
        Кликает по иконке корзины для перехода на страницу корзины.

        :return: None
        """
        cart_button_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.cart_button)
        )
        cart_button_element.click()
