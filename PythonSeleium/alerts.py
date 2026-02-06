import time


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

name = 'Pradeep'

driver = webdriver.Chrome()
driver.get('https://rahulshettyacademy.com/AutomationPractice/')
driver.maximize_window()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, '#name').send_keys(name)
driver.find_element(By.ID, 'alertbtn').click()
wait = WebDriverWait(driver, 10)
alert = wait.until(EC.alert_is_present())
time.sleep(2)
alert = driver.switch_to.alert
alertText = alert.text
assert name in alertText

alert.accept()
print(alertText)

