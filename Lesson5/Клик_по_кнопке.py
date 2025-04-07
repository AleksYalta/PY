import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get(" http://the-internet.herokuapp.com/add_remove_elements/")

button = driver.find_element(By.CSS_SELECTOR, 'button[onclick="addElement()"]')
for _ in range(5):
    button.click()
    time.sleep(0.5)
delete_buttons = driver.find_elements(By.CSS_SELECTOR, 'button[onclick="deleteElement()"]')
print(f"Количество кнопок Delete: {len(delete_buttons)}")
driver.quit()
