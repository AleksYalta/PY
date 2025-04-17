from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.saucedemo.com/"
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

    def open(self):
        self.driver.get(self.url)

    def login(self, username, password):
        username_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.username_input)
        )
        username_element.send_keys(username)

        password_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.password_input)
        )
        password_element.send_keys(password)

        login_button_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.login_button)
        )
        login_button_element.click()
