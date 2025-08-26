import time

from  selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://rahulshettyacademy.com/angularpractice/')
driver.maximize_window()
print(driver.title)
print(driver.current_url)
driver.find_element(By.NAME, 'email').click()
driver.find_element(By.NAME, 'email').send_keys('hello@gmail.com')
driver.find_element(By.ID, 'exampleInputPassword1' ).send_keys('123456')
driver.find_element(By.ID, 'exampleCheck1').click()
driver.find_element(By.XPATH, "//input[@type='submit']").click()
#Custom xpath - //tagname[@attribute='value']
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys('Pradeep')
# Custom css -   tagname[attribute='value']
driver.find_element(By.CSS_SELECTOR, '#inlineRadio1').click()   #ID
message = driver.find_element(By.CLASS_NAME, 'alert-success').text
print(message)

assert "Success" in message
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys('HelloPradeep')














time.sleep(5)
