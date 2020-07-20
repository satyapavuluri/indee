class Locators():
    '''
    This class is used to maintain all pages locators
    '''
    def __init__(self):
        pass

    # homepage
    search_textbox_id = "twotabsearchtextbox"
    search_button_class_name = "nav-input"
    midnight_green_color_phone_link_xpath = "//span[contains(text(), 'Midnight Green') and contains(text(), 'Carrier Locked')]"
    white_color_phone_link_xpath = "//span[contains(text(), 'White') and contains(text(), 'Carrier Locked')]"

    # product page
    delivery_location_link_id = "contextualIngressPtLabel_deliveryShortLine"
    zip_code_textbox_id = "GLUXZipUpdateInput"
    zip_code_apply_button_class_name = "a-button-input"
    zip_code_continue_button_id = "GLUXConfirmClose"
    invalid_zip_code_xpath = "//div[contains(text(), 'Please enter a valid US zip code')]"
    zip_code_done_button_name = "glowDoneButton"
    add_to_cart_button_id = "add-to-cart-button"
    currently_unavailable_text_xpath = "//h1[contains(text(), 'Currently unavailable.')]"

    # cart page
    proceed_to_checkout_button_id = "hlb-ptc-btn-native"
    amazon_sign_in_text_xpath = "//h1[contains(text(), 'Sign-In')]"
