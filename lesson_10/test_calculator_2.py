import allure
import pytest
from selenium import webdriver
from calcPageAllure import CalculatorPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@allure.title("Тестирование калькулятора: 7 + 8 = 15")
@allure.description("Проверка, что калькулятор корректно "
                    "складывает числа с задержкой")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
def test_calculator_addition(driver):
    page = CalculatorPage(driver)

    with allure.step("Открываем страницу калькулятора"):
        page.open()

    with allure.step("Устанавливаем задержку выполнения (45 секунд)"):
        page.set_delay(45)

    with allure.step("Вводим выражение 7 + 8"):
        page.click_button("7")
        page.click_button("+")
        page.click_button("8")
        page.click_button("=")

    with allure.step("Получаем результат вычисления и проверяем"):
        result = page.get_result(expected_result="15")
        assert result == "15", f"Expected 15, but got {result}"
