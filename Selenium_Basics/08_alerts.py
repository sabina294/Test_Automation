import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

driver.implicitly_wait(5)

driver.get("https://the-internet.herokuapp.com/javascript_alerts")

try:
    wait = WebDriverWait(driver, 20)
    js_alert = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[onclick='jsAlert()']")))
    js_alert.click()
    js_alert_title = driver.switch_to.alert.text
    print(js_alert_title)
    driver.switch_to.alert.accept() # click on ok
except Exception as e:
    print("Element 'JS Alert Button' not found with Explicit wait.")

try:
    wait = WebDriverWait(driver, 20)
    js_confirm_alert = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[onclick='jsConfirm()']")))
    js_confirm_alert.click()
    confirm_alert_title = driver.switch_to.alert.text
    print(confirm_alert_title)
    driver.switch_to.alert.dismiss() # click on Cancel
except Exception as e:
    print("Element 'JS Confirm Alert Button' not found with Explicit wait.")

try:
    wait = WebDriverWait(driver, 20)
    js_prompt_alert = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[onclick='jsPrompt()']")))
    js_prompt_alert.click()
    confirm_prompt_alert_title = driver.switch_to.alert.text
    print(confirm_prompt_alert_title)
    driver.switch_to.alert.send_keys("Test Automation")
    driver.switch_to.alert.accept()
except Exception as e:
    print("Element 'JS Prompt Alert Button' not found with Explicit wait.")
    driver.quit()