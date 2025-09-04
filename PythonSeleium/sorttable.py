import time

from selenium import webdriver
from selenium.webdriver.common.by import By
browserSortedVeggies = []

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.maximize_window()
driver.implicitly_wait(5)

#click on coloumn header
driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()  #finds the coloumn which has Veg/fruit name and clicks on the table.

#collect all veggielist - Browsersortedveggie list
veggieWebElements = driver.find_elements(By.XPATH, "//tr/td[1]")  #Collects all the first-column cells (td[1]) from each table row (tr).
for element in veggieWebElements:
    browserSortedVeggies.append(element.text)

originalBrowserSortedList = browserSortedVeggies.copy()

browserSortedVeggies.sort()
assert browserSortedVeggies == originalBrowserSortedList


time.sleep(5)



