import logging
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import  logging

# setup logging
logging.basicConfig(
    filename="14_file_upload.log",
    level= logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logging.info("Staring Browser Session...")

driver = webdriver.Chrome()
logging.info("Browser Launch Successfully.")

driver.maximize_window()
driver.implicitly_wait(5)

driver.get("https://practice.expandtesting.com/upload")
logging.info("URL Open Successfully.")


try:
    wait = WebDriverWait(driver, 20)
    file_path = "/home/sabina/personal/20250619_164746.jpg"
    logging.info("File Path Set Successfully")

    choose_file_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#fileInput")))
    choose_file_button.send_keys(file_path)
    logging.info("File Selected Successfully.")

    upload_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#fileSubmit")))
    upload_button.click()
    logging.info("Upload Button Clicked Succesfully..")

except Exception as e:
    logging.info("Element 'JS Alert Button' not found with Explicit wait.")

logging.info("Script Complete.")
