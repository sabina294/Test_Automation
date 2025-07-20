from selenium import webdriver

driver = webdriver.Chrome()

driver.maximize_window()


driver.get("https://google.com")

driver.quit()
