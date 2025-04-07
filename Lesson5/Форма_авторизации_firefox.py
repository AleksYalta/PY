import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/login")

time.sleep(5)

username = driver.find_element(By.ID, "username")
username.send_keys("tomsmith")

password = driver.find_element(By.ID, "password")
password.send_keys("SuperSecretPassword!")

login = driver.find_element(By.CLASS_NAME, "radius")
login.click()

time.sleep(3)

driver.quit()
