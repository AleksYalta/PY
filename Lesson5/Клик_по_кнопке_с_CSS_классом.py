import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/classattr")

time.sleep(5)

button = driver.find_element(By.CSS_SELECTOR, "button.btn-primary")
button.click()

print("Кнопка нажата")

time.sleep(5)

driver.quit()
