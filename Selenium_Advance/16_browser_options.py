from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# === Setup logging ===
logging.basicConfig(
    filename="logs/16_browser_options.log",
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# === Initialize Chrome Options ===
chrome_options = Options()
chrome_options.add_argument("--headless")  # run in headless mode (no browser window)
logging.info("Headless mode enabled for Chrome.")

# === Start browser session ===
logging.info("Starting browser session...")
driver = webdriver.Chrome(options=chrome_options)
logging.info("Chrome browser launched successfully.")

driver.maximize_window()
driver.implicitly_wait(5)

# === Open URL ===
url = "https://the-internet.herokuapp.com/javascript_alerts"
driver.get(url)
logging.info(f"URL '{url}' opened successfully.")

try:
    # === Wait for and click JS Alert button ===
    wait = WebDriverWait(driver, 20)
    js_alert = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[onclick='jsAlert()']")))
    js_alert.click()
    logging.info("Clicked on 'JS Alert' button.")

    # === Handle alert ===
    alert = driver.switch_to.alert
    alert_text = alert.text
    logging.info(f"Alert text: {alert_text}")
    alert.accept()
    logging.info("Alert accepted (OK clicked).")

except Exception as e:
    logging.error(f"Error handling JS Alert: {str(e)}")

# === End of script ===
driver.quit()
logging.info("Browser session ended. Script complete.")
