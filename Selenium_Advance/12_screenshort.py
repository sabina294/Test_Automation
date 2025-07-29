from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()

driver.implicitly_wait(5)

driver.get("https://www.google.com/")

driver.save_screenshot("Google.png")

print("Screenshort captured.")

driver.quit()