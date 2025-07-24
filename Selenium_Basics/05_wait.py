import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec

driver = webdriver.Chrome()
driver.maximize_window()

driver.implicitly_wait(5)

driver.get("https://epassport.gov.bd/onboarding")

try:
    bangladesh_no = driver.find_element(By.CSS_SELECTOR,"label[for='applying-bangladeshCommon.Labels.No']")
    bangladesh_no.click()

except Exception as e:
     print("Element 'No' not found with implicit wait.")

try:
    wait = WebDriverWait(driver, 10)
    bangladesh_yes = wait.until(Ec.presence_of_element_located((By.CSS_SELECTOR,"label[for='applying-bangladeshCommon.Labels.Yes']")))
    bangladesh_yes.click()

except Exception as e:
    print("Element 'Yes' not found with Explicit wait.")

try:
    wait = WebDriverWait(driver, 20)
    district = wait.until(Ec.presence_of_element_located((By.XPATH, "//input[@type='text']")))
    district.click()
    district.send_keys("DHAKA")
    time.sleep(2)
    district.send_keys(Keys.ARROW_DOWN)
    district.send_keys(Keys.ENTER)
    time.sleep(3)

except Exception as e:
    print("Element 'District' not found with Explicit wait.")
    time.sleep(5)


try:
    wait = WebDriverWait(driver, 20)
    police_station = wait.until(Ec.presence_of_element_located((By.XPATH, "(//input[@type='text'])[2]")))
    police_station.click()
    police_station.send_keys("BANANI")
    time.sleep(2)
    police_station.send_keys(Keys.ARROW_DOWN)
    police_station.send_keys(Keys.ENTER)

except Exception as e:
    print("Element 'police' not found with Explicit wait.")
    time.sleep(5)
    driver.quit()

