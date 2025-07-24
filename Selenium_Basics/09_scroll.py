import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

driver.implicitly_wait(5)

driver.get("https://www.apple.com/")

# Scroll the entire page
# driver.execute_script("window.scrollBy(0,2000);")

# Scroll to the bottom of page
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")

# Scroll to specific element
watch = driver.find_element(By.CSS_SELECTOR,".unit-link[href='/apple-watch-series-10/']")

driver.execute_script("arguments[0].scrollIntoView();", watch)
driver.quit()