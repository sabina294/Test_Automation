from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()

driver.implicitly_wait(5)

driver.get("https://the-internet.herokuapp.com/checkboxes")

try:
    wait = WebDriverWait(driver, 20)
    checkbox_option1 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input:nth-child(1)")))
    checkbox_option1.click()

except Exception as e:
    print("Element 'Checkbox' not found with Explicit wait.")

driver.quit()