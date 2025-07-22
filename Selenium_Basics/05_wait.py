
from selenium import webdriver
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
    wait = WebDriverWait(driver, 20)
    bangladesh_yes = wait.until(Ec.presence_of_element_located((By.CSS_SELECTOR,"label[for='applying-bangladeshCommon.Labels.Yes']")))
    bangladesh_yes.click()

except Exception as e:
    print("Element 'Yes' not found with Explicit wait.")

    







