from selenium import webdriver
from calculator_page import CalculatorPage


def test_calculator_addition():
    driver = webdriver.Chrome()
    try:
        page = CalculatorPage(driver)
        page.open()
        page.set_delay(45)
        page.click_button("7")
        page.click_button("+")
        page.click_button("8")
        page.click_button("=")

        result = page.get_result(timeout=45)
        assert result == "15", f"Expected 15, but got {result}"
    finally:
        driver.quit()
