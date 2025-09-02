import time

from  selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.maximize_window()
driver.find_element(By.ID, 'autosuggest').send_keys('ind')    #click and type ind
time.sleep(2)
countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")  #will show all the list of webelements
print(len(countries))      #will count the number of countries in the list

for country in countries:
    if country.text == "India":
        country.click()
        break

print(driver.find_element(By.ID, 'autosuggest').get_attribute('value'))  #to extract the value

#if we need to assert
# assert driver.find_element(By.ID, 'autosuggest').get_attribute('value') == 'India'












time.sleep(5)