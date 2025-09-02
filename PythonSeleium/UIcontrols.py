import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://rahulshettyacademy.com/AutomationPractice/')
driver.maximize_window()
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")

print(len(checkboxes))  #will printg list of checkbox for the above element

for checkbox in checkboxes:
    if checkbox.get_attribute('value') == 'option2':
        checkbox.click()
        assert checkbox.is_selected()   #it confirms checkbox is selected or not
        break


radiobuttons = driver.find_elements(By.CSS_SELECTOR, '.radioButton')
print(len(radiobuttons))
radiobuttons[2].click()
assert radiobuttons[2].is_selected()





time.sleep(5)


