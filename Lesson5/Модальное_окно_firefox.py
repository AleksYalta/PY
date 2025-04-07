import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/entry_ad")

time.sleep(5)

close_button = driver.find_element(By.CSS_SELECTOR, "#modal div.modal-footer p")

close_button.click()
print("Модальное окно закрыто")

time.sleep(3)

driver.quit()
