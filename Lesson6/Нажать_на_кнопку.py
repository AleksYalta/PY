from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/ajax")
button = driver.find_element(By.CSS_SELECTOR, "#ajaxButton")

button.click()

wait = WebDriverWait(driver, 15)
txt = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#content p")))
print(txt.text)

driver.quit()
