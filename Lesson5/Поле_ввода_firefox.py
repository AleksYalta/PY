import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/inputs")

time.sleep(5)

input_field = driver.find_element(By.CSS_SELECTOR, "input[type='number']")

input_field.send_keys("1000")
time.sleep(1)

input_field.clear()
time.sleep(1)

input_field.send_keys("999")

time.sleep(2)

driver.quit()
