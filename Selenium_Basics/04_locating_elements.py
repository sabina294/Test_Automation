import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()

driver.maximize_window()


driver.get("https://muntasir101.github.io/Modern-Bank-Portal/")

customer_registration_button = driver.find_element(By.CSS_SELECTOR,"homeRegisterCustomerBtnMain")

customer_registration_button.click()

time.sleep(2)

full_name = driver.find_element(By.CSS_SELECTOR,"#customerNameReg")
full_name.send_keys("Mr.Alice")