import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

file_path = "/Users/pradeepbaraik/Downloads/Test sheet Practise.xlsx"
fruit_name = "Apple"
driver = webdriver.Firefox()
driver.implicitly_wait(5)

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/upload-download-test/index.html")
driver.maximize_window()
driver.find_element(By.ID, "downloadButton").click()


file_input = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
file_input.send_keys(file_path)  #sending the path which file needs to be uploaded

toast_locator = (By.CSS_SELECTOR, ".Toastify__toast-body div:nth-child(2)")
WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(toast_locator))

print(driver.find_element(*toast_locator).text)


driver.find_element(By.XPATH, "//div[text()='"+fruit_name+"']/parent::div/parent::div/div[@id='cell-4-undefined']").text



time.sleep(5)

