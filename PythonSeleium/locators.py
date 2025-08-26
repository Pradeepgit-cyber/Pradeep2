import time


#from select import select

from  selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get('https://rahulshettyacademy.com/angularpractice/')
driver.maximize_window()
print(driver.title)
print(driver.current_url)
driver.find_element(By.NAME, 'email').click()
driver.find_element(By.NAME, 'email').send_keys('hello@gmail.com')
driver.find_element(By.ID, 'exampleInputPassword1' ).send_keys('123456')
driver.find_element(By.ID, 'exampleCheck1').click()
#Custom xpath - //tagname[@attribute='value']
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys('Pradeep')
# Custom css -   tagname[attribute='value']
driver.find_element(By.CSS_SELECTOR, '#inlineRadio1').click()   #ID
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys('HelloPradeep')

#static dropdown
dropdown = Select(driver.find_element(By.ID, 'exampleFormControlSelect1'))
dropdown.select_by_index(0)
time.sleep(2)
dropdown.select_by_visible_text('Female')





driver.find_element(By.XPATH, "//input[@type='submit']").click()

message = driver.find_element(By.CLASS_NAME, 'alert-success').text
print(message)

assert "Success" in message















time.sleep(5)
