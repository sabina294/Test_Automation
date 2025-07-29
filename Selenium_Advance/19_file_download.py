import os.path

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# setup logging
logging.basicConfig(
    filename="logs/16_file_download.log",
    level= logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# set download directory
download_dir = os.path.abspath("downloads")


# initialize Firefox Options
firefox_options = Options()
firefox_options.set_preference("browser.download.folderList",2)
firefox_options.set_preference("browser.download.dir", download_dir)
firefox_options.set_preference("browser.helperApps.neverAsk.saveToDisk","text/plain,application/pdf")
firefox_options.set_preference("browser.download.manager.showWhenStarting", False)

# Headless/Headed
# firefox_options.add_argument("--headless")
firefox_options.add_argument("--headed")
logging.info("Headed...")

logging.info("Staring Browser Session...")
driver = webdriver.Firefox(options=firefox_options)

logging.info("Browser Launch Successfully.")

driver.implicitly_wait(5)

driver.get("https://github.com/Muntasir101/Test_Automation_BITM06/blob/master/Selenium_Advance/logs/13_log.log")
logging.info("URL Open Successfully.")

driver.find_element(By.CSS_SELECTOR, ".octicon.octicon-download[aria-hidden='true'][focusable='false']").click()
logging.info("File Download successfully.")

logging.info("Script Complete.")

driver.quit()

logging.info("End Browser Session...")