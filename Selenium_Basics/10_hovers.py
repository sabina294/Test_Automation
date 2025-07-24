from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()

driver.implicitly_wait(5)

driver.get("https://the-internet.herokuapp.com/hovers")

try:
    wait = WebDriverWait(driver, 20)
    user1_profile = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "body > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(3) > img:nth-child(1)")))

    actions = ActionChains(driver)
    actions.move_to_element(user1_profile).perform()

except Exception as e:
    print("Element 'user1_profile' not found with Explicit wait.")