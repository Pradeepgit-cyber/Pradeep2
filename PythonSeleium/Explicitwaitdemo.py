import time

from numpy.ma.core import count
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
expectedList = ["Cucumber - 1 Kg", "Raspberry - 1/4 Kg", "Strawberry - 1/4 Kg"]
actualList = []


driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get('https://rahulshettyacademy.com/seleniumPractise/#/')
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR, '.search-keyword').send_keys('ber')
time.sleep(2)
results = driver.find_elements(By.XPATH, "//div[@class='products']/div")    #List of web elements.parent web element
count = len(results)
print(count)
assert count > 0  #Checks that at least one product was found.If not script stops with error.

for result in results:
    actualList.append(result.find_element(By.XPATH, "h4").text)  #adds product name in the actual list
    result.find_element(By.XPATH, "div/button").click()  #chaining the web element from parent to child.It finds button'Add to cart' button and clicks
print("Expected List:", expectedList)
print("Actual List:  ", actualList)

assert expectedList == actualList

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click() #Clicks on the shopping cart icon.
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()    #xpath by text.Clicks the "PROCEED TO CHECKOUT" button.


#sum validation
#Finds all product prices listed in the cart (the 5th column).
prices = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(5) p")
sum = 0 #adds prices of all products
for price in prices:
    sum = sum + int(price.text) #price.text gets the text value, which is converted to an integer and added to sum.
print(sum)   #prints the total sum
#Gets the total amount shown by the website and converts it to an integer.
totalAmount = int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)
assert sum == totalAmount  #Checks if your calculated sum matches the website’s total.

driver.find_element(By.CSS_SELECTOR, ".promocode").send_keys("rahulshettyacademy") #enters the promocode
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()  #clicks on the button
wait = WebDriverWait(driver,10) #Waits (up to 10 seconds) for the promo info message to appear.
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
print(driver.find_element(By.CLASS_NAME, "promoInfo").text) #prints the promo info message.

discountedAmount = float(driver.find_element(By.CSS_SELECTOR, ".discountAmt").text)
assert totalAmount > discountedAmount
print(discountedAmount)


time.sleep(2)












