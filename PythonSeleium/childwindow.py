import time

from numpy.ma.core import count
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get('https://the-internet.herokuapp.com/windows')
driver.maximize_window()
driver.find_element(By.LINK_TEXT, "Click Here").click()
windowsOpened = driver.window_handles       #Gets the list of all open windows.

driver.switch_to.window(windowsOpened[1])    #child window - Switches focus from the parent window to the child window (so now actions will happen in the new window).
print(driver.find_element(By.TAG_NAME, "h3").text)  #prints the text from child window
driver.close()  #will close child window
driver.switch_to.window(windowsOpened[0])    #switches back to parent window

    #Checks if the heading <h3> in the parent window matches the expected text “Opening a new window”.
assert "Opening a new window" == driver.find_element(By.TAG_NAME, "h3").text






time.sleep(2)


