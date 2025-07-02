import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
test_results = []
driver.get("https://salesright.squareboat.info/")
driver.maximize_window()
time.sleep(3)

# Test Case 1
try:
    driver.find_element(By.XPATH, value="/html/body/section/div/div[1]/form/div[1]/div/input").send_keys("nilesh-admin@gmail.com")
    driver.find_element(By.XPATH, value="/html/body/section/div/div[1]/form/div[2]/div/input").send_keys("TEst@1234")
    time.sleep(3)
    driver.find_element(By.XPATH, value="/html/body/section/div/div[1]/form/button[1]").click()
    test_results.append("Test Case 1: Failed (Wrong Password)")
except Exception as e:
    test_results.append(f"Test Case 1: Failed (Exception: {str(e)})")

# Clear inputs
time.sleep(5)
driver.find_element(By.XPATH, value="/html/body/section/div/div[1]/form/div[1]/div/input").clear()
driver.find_element(By.XPATH, value="/html/body/section/div/div[1]/form/div[2]/div/input").clear()
time.sleep(5)

# Test Case 2
try:
    driver.find_element(By.XPATH, value="/html/body/section/div/div[1]/form/div[1]/div/input").send_keys("niles-admin@gmail.com")
    driver.find_element(By.XPATH, value="/html/body/section/div/div[1]/form/div[2]/div/input").send_keys("Admin@1234")
    time.sleep(3)
    driver.find_element(By.XPATH, value="/html/body/section/div/div[1]/form/button[1]").click()
    test_results.append("Test Case 2: Failed (Invalid Email ID)")
except Exception as e:
    test_results.append(f"Test Case 2: Failed (Exception: {str(e)})")

# Clear inputs
time.sleep(5)
driver.find_element(By.XPATH, value="/html/body/section/div/div[1]/form/div[1]/div/input").clear()
driver.find_element(By.XPATH, value="/html/body/section/div/div[1]/form/div[2]/div/input").clear()
time.sleep(3)

#  Test Case 3
try:
    driver.find_element(By.XPATH, value="/html/body/section/div/div[1]/form/div[1]/div/input").send_keys("nilesh-admin@gmail.com")
    driver.find_element(By.XPATH, value="/html/body/section/div/div[1]/form/div[2]/div/input").send_keys("Admin@1234")
    driver.find_element(By.XPATH, value="/html/body/section/div/div[1]/form/button[1]").click()
    time.sleep(5)

    if "dashboard" in driver.current_url.lower() or "Dashboard" in driver.page_source:
        test_results.append("Test Case 3: Passed")

    else:
        test_results.append("Test Case 3: Failed (Dashboard not loaded)")

except Exception as e:
    test_results.append(f"Test Case 3: Failed (Exception: {str(e)})")

# Print all test results at once
print("\n".join(test_results))
