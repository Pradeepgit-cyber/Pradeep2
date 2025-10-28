import pytest      #testing framework
from selenium import webdriver     #controls the webbrowser
from  selenium.webdriver.chrome.service import Service  #manages the chrome driver

#This code lets you choose which browser to run your tests in by passing a command-line argument.
#If you don’t specify one, it will use Chrome by default.
#If we need to use firefox browser we just need to send command --browser name firefox.
#If nothing found in the command it will pick teh default browser chrome else it will run in firefox
def pytest_addoption(parser):            #it modifies the pytest
    parser.addoption("--browser_name", action="store", default="chrome", help="browser selection")


@pytest.fixture(scope="function")
def browserInstance(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
      driver = webdriver.Chrome()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
        driver.implicitly_wait(5)
    yield driver


