import json
import os
import sys

import pytest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from pageObjects.login import LoginPage
test_data_path = '../data/test_e2eTestFramework.json'   #where is my json file stored.
with open(test_data_path) as f:           #open json file and name it as f. f is a file object here
    test_data = json.load(f)              #data in the jsonfile to be coverted in python dictionary
    test_list = test_data["data"]         #Take the value of the ‘data’ key from the dictionary and store it in test_list

@pytest.mark.smoke
@pytest.mark.parametrize("test_list_item", test_list)   #test_list - no of items in the data, test_list_item - run every time and keep it in variable(test_list_item)
def test_e2e(browserInstance,test_list_item):
    driver = browserInstance
    loginPage = LoginPage(driver)
    print(loginPage.getTitle())
    shop_page = loginPage.Login(test_list_item["userEmail"], test_list_item["userPassword"])
    shop_page.add_product_to_cart(test_list_item["productname"])
    print(shop_page.getTitle())
    checkout_confirmation = shop_page.goToCart()
    checkout_confirmation.checkout()
    checkout_confirmation.enter_delivery_address("india")
    checkout_confirmation.validate_order()

    #  //a[contains(@href,'shop')]  - xpath     a[href*='shop']  - css







