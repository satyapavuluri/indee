from src.lib.locators.locators import Locators

LOCATORS = Locators()

class Product():
    '''
    Product page (Page which redirects when we select the
    item from the home page)
    '''
    def __init__(self, driver):
        '''
        Initializing with the driver
        :param driver:
        '''
        self.driver = driver

    def enter_postal_code(self, text):
        '''
        This function is used to click in delivery location link
        and enter zip code into textbox
        :param element:
        :param text:
        :return:
        '''
        self.driver.find_element_by_id(
            LOCATORS.delivery_location_link_id).click()
        self.driver.find_elements_by_id(
            LOCATORS.zip_code_textbox_id).send_keys(text)

    def click_on_zip_code_apply(self):
        '''
        This function is used to click in "Apply" button
        after enter the zip code into text box
        :return:
        '''
        self.driver.find_element_by_class_name(
            LOCATORS.zip_code_apply_button_class_name).click()

    def click_on_zip_code_continue(self):
        '''
        This function is used to click in "Continue" button
        :return:
        '''
        self.driver.find_element_by_id(
            LOCATORS.zip_code_continue_button_id).click()

    def click_on_add_to_cart_button(self):
        '''
        This function is used to click in "Add to cart" button
        :return:
        '''
        self.driver.find_element_by_id(
            LOCATORS.add_to_cart_button_id).click()

    def click_on_proceed_to_checkout(self):
        '''
        This function is used to click in "proceed to checkout" button
        :return:
        '''
        self.driver.find_element_by_id(
            LOCATORS.proceed_to_checkout_button_id).click()

    def currently_unavailable_text(self):
        '''
        This function is used to find out "Currently unavailable" text
        :return:
        '''
        return self.driver.find_elements_by_xpath(
            LOCATORS.currently_unavailable_text_xpath)