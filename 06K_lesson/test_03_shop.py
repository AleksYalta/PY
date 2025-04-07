from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def test_shop_authorization():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    try:
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        products = [
            "add-to-cart-sauce-labs-backpack",
            "add-to-cart-sauce-labs-bolt-t-shirt",
            "add-to-cart-sauce-labs-onesie"
        ]
        for product_id in products:
            driver.find_element(By.ID, product_id).click()

        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        driver.find_element(By.ID, "checkout").click()

        driver.find_element(By.ID, "first-name").send_keys("Александр")
        driver.find_element(By.ID, "last-name").send_keys("Картагузов")
        driver.find_element(By.ID, "postal-code").send_keys("298600")
        driver.find_element(By.ID, "continue").click()

        total = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME,
                                              "summary_total_label"))
        )
        total_text = total.text

        assert "$58.29" in total_text, \
            f"Ожидалась сумма $58.29, но получено '{total_text}'"

        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID,
                                                "this-element-does-not-exist"))
            )
        except TimeoutException:
            pass

    finally:
        driver.quit()
