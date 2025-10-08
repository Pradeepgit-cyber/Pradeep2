from pydoc import text

from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")  #chrome will maximize the screen in the background
chrome_options.add_argument("headless")   #chrome will run without opening the browser.
chrome_options.add_argument("--ignore-certificate-errors")    #chrome will ignore all the certification errors like ssl.



driver = webdriver.Chrome(options=chrome_options)
driver.get("https://google.com")

print(driver.title)


