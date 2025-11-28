import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.implicitly_wait(5)

# driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")   #will scroll till bottom.
driver.execute_script("window.scrollBy(0,700);")   #will scroll till certain limit
driver.get_screenshot_as_file("screen.png")#will take screenshots
print("Screenshot Saved")



time.sleep(3)
