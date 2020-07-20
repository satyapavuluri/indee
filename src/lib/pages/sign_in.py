from lib.locators.locators import Locators

LOCATORS = Locators()

class SignIn():
    '''
    Amazon sign-in page
    '''
    def __init__(self, driver):
        '''
        Initializing the with driver
        :param driver:
        '''
        self.driver = driver

    def sign_in_text(self):
        '''
        This function is used to check that "Sing-In" text is present or not
        :return: Boolean value
        '''
        return self.driver.find_element_by_xpath(
            LOCATORS.amazon_sign_in_text_xpath).isDisplayed()