# import os
#
# import pytest      #testing framework
# from outcome import capture
# from selenium import webdriver     #controls the webbrowser
# from  selenium.webdriver.chrome.service import Service  #manages the chrome driver
# driver = None
#
# #This code lets you choose which browser to run your tests in by passing a command-line argument.
# #If you don’t specify one, it will use Chrome by default.
# #If we need to use firefox browser we just need to send command --browser name firefox.
# #If nothing found in the command it will pick teh default browser chrome else it will run in firefox
#
# def pytest_addoption(parser):            #it modifies the pytest
#     parser.addoption("--browser_name", action="store", default="chrome", help="browser selection")
#
#
# @pytest.fixture(scope="function")
# def browserInstance(request):
#     global driver
#     browser_name = request.config.getoption("browser_name")
#     if browser_name == "chrome":
#         options = webdriver.ChromeOptions()
#         # Disable Chrome password manager and related popups
#         # Launch in Incognito mode
#         options.add_argument("--incognito")
#         driver = webdriver.Chrome(options=options)
#         driver.implicitly_wait(5)
#     elif browser_name == "firefox":
#         driver = webdriver.Firefox()
#         driver.implicitly_wait(5)
#     else:
#         raise ValueError(f"Unsupported browser: {browser_name}")
#     driver.get("https://rahulshettyacademy.com/loginpagePractise/")
#     yield driver    #before test function execution
#     driver.quit()   #post your test function execution
#
#
# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item):
#     pytest_html = item.config.pluginmanager.getplugin('html')
#     outcome = yield
#     report = outcome.get_result()
#     extra = getattr(report, 'extra', [])
#
#     if report.when == 'call' or report.when == 'setup':
#         xfail = hasattr(report, 'xfail')
#         if (report.failed and xfail) or (report.failed and not xfail):
#             reports_dir = os.path.join(os.path.dirname(__file__), "reports")
#             file_name = os.path.join(reports_dir, report.nodeid.replace(" ", "_")) + ".html"
#             print("Writing report to " + file_name)
#             Capture_screenshot(file_name)
#             if file_name:
#                 html = open(file_name).read()
#                 extra.append(html)
#         report.extra = extra
#
# def Capture_screenshot(file_name):
#     driver.get_screenshot_as_file(file_name)

import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

driver = None

def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome",
                     help="browser selection")


@pytest.fixture(scope="function")
def browserInstance(request):
    global driver
    browser_name = request.config.getoption("browser_name")

    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--incognito")
        driver = webdriver.Chrome(options=options)
        driver.implicitly_wait(5)

    elif browser_name == "firefox":
        driver = webdriver.Firefox()
        driver.implicitly_wait(5)

    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    yield driver
    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Attach screenshot to pytest-html report when a test FAILS.
    """
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("browserInstance")
        if driver is None:
            return

        # Create screenshot directory
        screenshots_dir = os.path.join(os.path.dirname(__file__), "reports", "screenshots")
        os.makedirs(screenshots_dir, exist_ok=True)

        # File name for screenshot
        file_name = report.nodeid.replace("/", "_").replace("::", "_") + ".png"
        file_path = os.path.join(screenshots_dir, file_name)

        # Capture screenshot
        driver.save_screenshot(file_path)

        # Attach screenshot to HTML report
        extra = getattr(report, "extra", [])
        extra.append(pytest_html.extras.image(file_path))
        report.extra = extra

