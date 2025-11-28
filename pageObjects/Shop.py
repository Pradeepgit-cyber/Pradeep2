from selenium.webdriver.common.by import By     #is used to locate the web elements

from pageObjects.Checkout_confirmation import Checkout_Confirmation      #Different checkout page
from utils.browserutils import BrowserUtils


class Shoppage(BrowserUtils):
    def __init__(self, driver):
        super().__init__(driver)#constructor - object from a class
        self.driver = driver             #controls the browser of selenium
        self.shop_link = (By.CSS_SELECTOR, "a[href*='shop']")      #redirect to the shop link locator
        self.product_cards = (By.XPATH, "//div[@class='card h-100']")    #to locate all the products
        self.checkout_button = (By.CSS_SELECTOR, "a[class*='btn-primary']")


    def add_product_to_cart(self,product_name):
        self.driver.find_element(*self.shop_link).click()
        products = self.driver.find_elements(*self.product_cards)

        for product in products:
            productname = product.find_element(By.XPATH, "div/h4/a").text
            if productname == "product_name":
                product.find_element(By.XPATH, "div/button").click()


    def goToCart(self):
        self.driver.find_element(*self.checkout_button).click()
        checkout_confirmation = Checkout_Confirmation(self.driver)
        return checkout_confirmation




