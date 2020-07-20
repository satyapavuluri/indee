from src.lib.locators.locators import Locators

LOCATORS = Locators()

class HomePage():
    '''
    Amazon home page
    '''
    def __init__(self, driver):
        '''
        Initializing with the driver
        :param driver:
        '''
        self.driver = driver

    def search_box(self, text):
        '''
        This function is used to locate the search box and enter text
        :param text:
        :return:
        '''
        self.driver.find_element_by_id(
            LOCATORS.search_textbox_id).send_keys(text)

    def search_botton(self):
        '''
        This function is used to click in search button
        :param element:
        :return:
        '''
        self.driver.find_element_by_class_name(
            LOCATORS.search_button_class_name).click()

    def midnight_green_color_phone_elements(self):
        '''
        This function is used to check "Midnight green color phones"
        are present or not
        :return: Boolean value
        '''
        return self.driver.find_elements_by_xpath(
            LOCATORS.midnight_green_color_phone_link_xpath)

    def white_color_phone_elements(self):
        '''
        This function is used to check "White color phones"
        are present or not
        :return: Boolean value
        '''
        return self.driver.find_elements_by_xpath(
            LOCATORS.white_color_phone_link_xpath)

    def click_on_midnight_green_carrier_locked_link(self):
        '''
        This function is used to locate "Midnight green carrier locked"
        phone link
        :return:
        '''
        self.driver.find_element_by_xpath(
            LOCATORS.midnight_green_color_phone_link_xpath).click()

    def click_on_white_carrier_locked_link(self):
        '''
        This function is used to locate "white carrier locked"
        phone link
        :return:
        '''
        self.driver.find_element_by_xpath(
            LOCATORS.white_color_phone_link_xpath).click()