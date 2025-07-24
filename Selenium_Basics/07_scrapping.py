import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

driver.implicitly_wait(5)

driver.get("https://www.epassport.gov.bd/onboarding")

try:
    bangladeshi_no = driver.find_element(By.CSS_SELECTOR, "label[for='applying-bangladeshCommon.Labels.No']")
    bangladeshi_no.click()
except Exception as e:
    print("Element 'No' not found with implicit wait.")

try:
    wait = WebDriverWait(driver, 20)
    bangladeshi_yes = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "label[for='applying-bangladeshCommon.Labels.Yes']")))
    bangladeshi_yes.click()
except Exception as e:
    print("Element 'Yes' not found with Explicit wait.")


try:
    wait = WebDriverWait(driver, 20)
    district = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='text']")))
    district.click()
    district.send_keys("Dhaka")
    time.sleep(2)
    district.send_keys(Keys.ARROW_DOWN)
    district.send_keys(Keys.ENTER)
    time.sleep(2)
except Exception as e:
    print("Element 'District' not found with Explicit wait.")


try:
    wait = WebDriverWait(driver, 20)
    police_station = wait.until(EC.presence_of_element_located((By.XPATH, "(//input[@type='text'])[2]")))
    police_station.click()
    police_station.send_keys("BANANI")
    time.sleep(2)
    police_station.send_keys(Keys.ARROW_DOWN)
    police_station.send_keys(Keys.ENTER)
except Exception as e:
    print("Element 'Police Station' not found with Explicit wait.")

# Scraping
try:
    expected_passport_office_name = "AGARGAON"

    wait = WebDriverWait(driver, 20)
    actual_passport_office = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".rpo-control__content")))
    actual_passport_office_name = actual_passport_office.text # text scrap
    if expected_passport_office_name == actual_passport_office_name:
        print(f"Passport Office Name:{actual_passport_office_name} Found.Test Passed.")
    else:
        print(f"Passport Office Name:{expected_passport_office_name} not Found.Test Failed!!!")

except Exception as e:
    print("Element 'Passport office' not found with Explicit wait.")

try:
    wait = WebDriverWait(driver, 20)
    continue_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[type='submit']")))
    continue_button.click()

except Exception as e:
    print("Element 'Continue Button' not found with Explicit wait.")
    time.sleep(20)

