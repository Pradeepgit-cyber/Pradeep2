import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# from Login import test_results

driver = webdriver.Chrome()
driver.get("https://salesright.squareboat.info/")
driver.maximize_window()
driver.find_element(By.XPATH, "/html/body/section/div/div[1]/form/div[1]/div/input").send_keys("nilesh-admin@gmail.com")
driver.find_element(By.XPATH, "/html/body/section/div/div[1]/form/div[2]/div/input").send_keys("Admin@1234")
driver.find_element(By.XPATH, "/html/body/section/div/div[1]/form/button[1]").click()

input("Login sucessfull")
time.sleep(3)
driver.find_element(By.LINK_TEXT, "Deals").click()
time.sleep(3)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/main/div[1]/div[2]/div[1]/span/input").send_keys("Joseph Cvek")




