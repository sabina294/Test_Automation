from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

# === Ensure logs directory exists ===
os.makedirs("logs", exist_ok=True)

# === Setup logging ===
logging.basicConfig(
    filename="18_browser_switch.log",
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# === Initialize Chrome Options ===
chrome_options = Options()

# Headed mode (default) — No need to add "--headed"
logging.info("Running in headed mode.")

# Window size
chrome_options.add_argument("--window-size=700,600")
logging.info("Browser window size set to 700x600.")

# Incognito mode
chrome_options.add_argument("--incognito")
logging.info("Chrome running in incognito mode.")

# === Launch Chrome ===
logging.info("Starting browser session...")
driver = webdriver.Chrome(options=chrome_options)
logging.info("Chrome browser launched successfully.")

driver.implicitly_wait(5)

# === Open target page ===
url = "https://the-internet.herokuapp.com/javascript_alerts"
driver.get(url)
logging.info(f"URL '{url}' opened successfully.")

# === Handle JavaScript Alert ===
try:
    wait = WebDriverWait(driver, 20)
    js_alert = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[onclick='jsAlert()']")))
    js_alert.click()
    logging.info("Clicked on JS Alert button.")

    alert_text = driver.switch_to.alert.text
    logging.info(f"Alert text: {alert_text}")

    driver.switch_to.alert.accept()
    logging.info("Alert accepted.")

except Exception as e:
    logging.error(f"Failed to handle JS Alert: {e}")

# === Close Browser ===
driver.quit()
logging.info("Browser session ended. Script complete.")
