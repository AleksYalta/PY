from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_calc():
    driver = webdriver.Chrome()
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    try:
        delay_input = driver.find_element(By.ID, 'delay')
        delay_input.clear()
        delay_input.send_keys('45')

        driver.find_element(By.XPATH, "//span[text()='7']").click()
        driver.find_element(By.XPATH, "//span[text()='+']").click()
        driver.find_element(By.XPATH, "//span[text()='8']").click()
        driver.find_element(By.XPATH, "//span[text()='=']").click()

        WebDriverWait(driver, 50).until(
            EC.invisibility_of_element_located((By.ID, 'spinner'))
        )

        result_field = driver.find_element(By.CLASS_NAME, 'screen')
        assert result_field.text == '15', \
            f"expected result '15', but got '{result_field.text}'"

    finally:
        driver.quit()
