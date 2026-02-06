import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://practice.cydeo.com/iframe")
driver.maximize_window()
driver.implicitly_wait(5)

driver.switch_to.frame("mce_0_ifr")   #switch inside a iframe
time.sleep(2)
driver.find_element(By.ID, "tinymce").clear()   #clears the text inside the iframe
driver.find_element(By.ID, "tinymce").send_keys("I am able to automate frames") #types the text inside the iframe
time.sleep(5)
driver.switch_to.default_content()  #switch back to main frame

#validates and prints the text from the main frame
print(driver.find_element(By.XPATH, "//h3[text()='An iFrame containing the TinyMCE WYSIWYG Editor']").text)



time.sleep(2)
