import allure
from selenium import webdriver
from calcPageAllure import CalculatorPage


@allure.title("Проверка сложения 7 + 8 в калькуляторе")
@allure.description("Проверяем, что калькулятор корректно складывает "
                    "7 и 8 с учётом задержки в 45 секунд.")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
def test_calculator_addition():
    driver = webdriver.Chrome()
    try:
        with allure.step("Открываем страницу калькулятора"):
            page = CalculatorPage(driver)
            page.open()

        with allure.step("Устанавливаем задержку 45 секунд"):
            page.set_delay(45)

        with allure.step("Нажимаем на кнопки: 7 + 8 ="):
            page.click_button("7")
            page.click_button("+")
            page.click_button("8")
            page.click_button("=")

        with allure.step("Получаем результат и проверяем его"):
            result = page.get_result(timeout=45)
            assert result == "15", f"Expected 15, but got {result}"

    finally:
        driver.quit()
