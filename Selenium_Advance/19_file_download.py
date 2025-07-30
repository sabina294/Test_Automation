import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import logging

# === Setup logging ===
logging.basicConfig(
    filename="19_file_download.log",
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# === Set download directory ===
download_dir = os.path.abspath("downloads")
os.makedirs(download_dir, exist_ok=True)

# === Initialize Chrome Options ===
chrome_options = Options()

# Set Chrome preferences to allow automatic download
prefs = {
    "download.default_directory": download_dir,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
}
chrome_options.add_experimental_option("prefs", prefs)

# Headed mode (default)
logging.info("Headed mode enabled.")

# === Start Chrome browser ===
logging.info("Starting browser session...")
driver = webdriver.Chrome(options=chrome_options)
logging.info("Chrome browser launched successfully.")

driver.implicitly_wait(5)

# === Navigate to raw file URL directly for download ===
raw_file_url = "https://raw.githubusercontent.com/Muntasir101/Test_Automation_BITM06/master/Selenium_Advance/logs/13_log.log"
driver.get(raw_file_url)
logging.info("Navigated to raw file URL.")

# Wait briefly to allow download to complete
time.sleep(5)

# === Check if file downloaded ===
downloaded_file_path = os.path.join(download_dir, "13_log.log")
if os.path.exists(downloaded_file_path):
    logging.info("File downloaded successfully: 13_log.log")
else:
    logging.error("File not found after download attempt.")

# === Cleanup ===
driver.quit()
logging.info("Browser session ended. Script complete.")
