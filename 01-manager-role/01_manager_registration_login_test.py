import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://muntasir101.github.io/Modern-Bank-Portal/")
time.sleep(3)

manager_registration = driver.find_element(By.CSS_SELECTOR,"#homeRegisterManagerBtn")

manager_registration.click()

full_name = driver.find_element(By.CSS_SELECTOR, "#managerNameReg")
full_name.send_keys("Sabina")
time.sleep(3)

email = driver.find_element(By.CSS_SELECTOR, "#managerEmailReg")
email.send_keys("test@example.com")
time.sleep(3)

password = driver.find_element(By.CSS_SELECTOR, "#managerPasswordReg")
password.send_keys("123456")
time.sleep(3)

manager_registration = driver.find_element(By.CSS_SELECTOR, "form[id='managerRegisterForm'] button[type='submit']")
manager_registration.click()

time.sleep(4)

back_home = driver.find_element(By.CSS_SELECTOR, "form[id='managerRegisterForm'] button[type='button']")
back_home.click()

time.sleep(4)

manager_login = driver.find_element(By.CSS_SELECTOR,"#homeLoginManagerBtn")
manager_login.click()

email = driver.find_element(By.CSS_SELECTOR, "#loginEmail")
email.send_keys("test@example.com")
time.sleep(3)

password = driver.find_element(By.CSS_SELECTOR, "#loginPassword")
password.send_keys("123456")
time.sleep(3)

manager_login = driver.find_element(By.CSS_SELECTOR, "form[id='loginForm'] button[type='submit']")
manager_login.click()

time.sleep(4)

