import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from lib.pages.home_page import HomePage
from lib.pages.product_page import Product
from lib.pages.sign_in import SignIn
from lib.utils import info_log, warning_log
from selenium import webdriver
import time
import pytest

CHROME_DRIVER_PATH = os.path.normpath(
    os.path.dirname(os.path.dirname(__file__)) +
    "../../tools/selenium_drivers/chromedriver")

class TestAddIphoneToCart:
    '''
    Test class
    '''
    @pytest.fixture()
    def test_setup(self):
        '''
        Setup function:
        1. Initializes chrome driver, HomePage, Product, SignIn
        2. Maximizes browser window
        3. Implicit wait for 10 sec
        4. Yields after test function execution finishes
        :return: screen shot
        '''
        global driver, homepage, productpage, signin_page
        driver = webdriver.Chrome(CHROME_DRIVER_PATH)
        homepage = HomePage(driver)
        productpage = Product(driver)
        signin_page = SignIn(driver)
        driver.maximize_window()
        driver.implicitly_wait(10)
        yield
        driver.save_screenshot("output.png")
        time.sleep(3)
        driver.close()
        driver.quit()
        info_log("Test case execution is successful !!!")

    def element_present(self, element, text):
        '''
        This function is used to check elements are present in the page or not
        :param element: element
        :param text: text to print in the log
        :return:
        '''
        if len(element) > 0:
            info_log("{} are available !!!".format(text))
        else:
            info_log("{} are not available !!!".format(text))

    def test(self, test_setup):
        '''
        Test function: End to end execution
        Steps:
        1. Enter amazon.com url into browser
        2. Enter "Apple iPhone 11 pro max" text into search box
        3. Click in search button
        4. Search "Midnight green color with carrier locked"
        and "White color with carrier locked" are present
        5. Check availability of items: if items are unavailable
        printing log, else do follow steps
        6. Click on "Deliver to" link and enter zip code
        7. Click on "Apply" button and click on "Continue"
        8. Click on "Add to cart" button
        9. Click on "Proceed to check out"
        10. Check page is redirecting to "Sign-In" page
        :param test_setup:
        :return:
        '''
        driver.get("https://www.amazon.com/")
        homepage.search_box("Apple iPhone 11 pro max")
        homepage.search_botton()
        self.element_present(
            homepage.midnight_green_color_phone_elements(),
            "Midnight green color with carrier locked")
        self.element_present(
            homepage.white_color_phone_elements(),
            "White color with carrier locked")
        homepage.click_on_midnight_green_carrier_locked_link()
        if len(productpage.currently_unavailable_text()) > 0:
            warning_log("Midnight green color with carrier "
                        "locked are currently unavailable !!!")
        else:
            productpage.enter_postal_code("90401")
            productpage.click_on_zip_code_apply()
            productpage.click_on_zip_code_continue()
            productpage.click_on_add_to_cart_button()
            productpage.click_on_proceed_to_checkout()
            assert signin_page.sign_in_text()
