import time

from numpy.ma.core import count
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get('https://rahulshettyacademy.com/AutomationPractice/')
driver.maximize_window()

action = ActionChains(driver)
# action.click_and_hold().perform()  #for long press
# action.context_click().perform()  #right click on any element
# action.double_click().perform()  #need to double click on any element
# action.drag_and_drop().perform()
time.sleep(5)
action.move_to_element(driver.find_element(By.ID, "mousehover")).perform()
# action.context_click(driver.find_element(By.LINK_TEXT, "Top")).perform()
action.move_to_element(driver.find_element(By.LINK_TEXT, "Reload")).click()



time.sleep(2)