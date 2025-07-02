import time
from datetime import datetime
from turtledemo.penrose import start

import dashboard
from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

driver.get("https://salesright.squareboat.info/")
driver.maximize_window()
time.sleep(3)
driver.find_element(By.XPATH, value="/html/body/section/div/div[1]/form/div[1]/div/input").send_keys("nilesh-admin@gmail.com")
driver.find_element(By.XPATH, value="/html/body/section/div/div[1]/form/div[2]/div/input").send_keys("Admin@1234")
time.sleep(5)
driver.find_element(By.XPATH, value="/html/body/section/div/div[1]/form/button[1]").click()
# input("Login Successfull")
time.sleep(5)
driver.find_element(By.XPATH, "/html/body/div/aside/div/div/ul/li[2]").click()
time.sleep(5)
driver.find_element(By.XPATH, "/html/body/div/div/div/main/div[1]/div[2]/div[1]/div/div").click()
time.sleep(10)
driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div/div[1]/button[2]").click()
driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div/div[2]/table/tbody/tr[1]/td[7]").click()
driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div/div[2]/table/tbody/tr[5]/td[6]").click()
time.sleep(5)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/main/div[1]/div[2]/div[2]/div[1]").click()
time.sleep(5)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/main/div[1]/div[2]/div[2]/div[1]/div/span/div/div").click()
driver.find_element(By.ID, "rc_select_0").send_keys("United States")
time.sleep(5)
driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/div/div/div/div").click()
driver.find_element(By.ID, "rc_select_0").send_keys("Angola")
time.sleep(5)
driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/div/div/div/div").click()
time.sleep(3)
driver.find_element(By.XPATH, "/html/body/div/div/div/main/div[1]/div[2]/div[1]/div/button").click()
driver.find_element(By.XPATH, "//a[text()='Admin']").click()
# driver.find_element(By.XPATH, '//a[@href= "/dashboard/admin"]').click()
time.sleep(5)
driver.find_element(By.XPATH, "(//button/span[@class='ant-btn-icon'])[2]").click()
time.sleep(3)
driver.find_element(By.XPATH, "//input[@name='firstName']").send_keys("Pradeep")
driver.find_element(By.XPATH, "//input[@placeholder='Enter last name']").send_keys("Test")

input("Successfull")

