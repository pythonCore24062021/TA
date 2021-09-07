from selenium.common.exceptions import TimeoutException
from HW.atarasov.pages.base_page import BasePage
from HW.atarasov.data.constants import LANDING_PAGE_URL


class LandingPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def go_to_landing_page(self):
        self.navigate_to_url(LANDING_PAGE_URL)

    def change_currency_using_xpath(self, currency_text):
        if currency_text != '€ Euro' or \
                currency_text != '£ Pound Sterling' or \
                currency_text != '$ US Dollar':
            raise ValueError('Illegible option')
        self.click_on_element('CURRENCY_XPATH_DD')
        self.click_on_element(self.get_value_in_dropdown_using_xpath(currency_text), loc=True)

    def change_currency_using_css(self, currency_name):
        if currency_name != 'EUR' and \
                currency_name != 'GBP' and \
                currency_name != 'USD':
            raise ValueError('Illegible option')
        self.click_on_element('CURRENCY_CSS_DD')
        self.click_on_element(self.get_value_in_dropdown_using_css(currency_name), loc=True)

    def verify_currency_change(self, currency_name):
        if currency_name != 'EUR' and \
                currency_name != 'GBP' and \
                currency_name != 'USD':
            raise ValueError('Illegible option')
        open_cart_text = self.get_text_of_element('CART_TOTAL_XPATH_BUTTON')
        if currency_name == 'EUR' and open_cart_text == '0 item(s) - 0.00€' or \
                currency_name == 'GBP' and open_cart_text == '0 item(s) - £0.00' or \
                currency_name == 'USD' and open_cart_text == '0 item(s) - $0.00':
            return True
        else:
            return False

    def make_search_request(self, word):
        self.enter_input_to_field('SEARCH_CSS_FIELD', word)
        return self.click_on_element('SEARCH_CSS_BUTTON')

    def fetch_all_search_results_on_the_page(self):
        return self.get_text_of_elements('SEARCH_RESULTS_LIST')

    def fetch_all_cart_items_on_the_page(self):
        return self.get_text_of_elements('CART_ITEMS_LIST')

    def verify_search_results(self, set_with_expected_results):
        set_with_actual_results = set(self.fetch_all_search_results_on_the_page())
        if set_with_expected_results.issubset(set_with_actual_results):
            return True
        else:
            return False

    def add_item_to_cart(self, item_name):
        self.click_on_element(self.get_specific_search_result_element(item_name), loc=True)
        self.click_on_element('ADD_TO_CART_CSS_BUTTON')
        try:
            self.get_text_of_element('SIZE_REQUIRED_CSS_WARNING')
            self.click_on_element('SIZE_CSS_DD')
            self.click_on_element('SIZE_MEDIUM_CSS_OPTION')
            self.click_on_element('ADD_TO_CART_CSS_BUTTON')
            self.click_on_element('CLOSE_ALERT_CSS_BUTTON')
            return self.go_to_landing_page()
        except TimeoutException:
            self.go_to_landing_page()

    def go_to_cart(self):
        self.click_on_element('CART_TOTAL_CSS_BUTTON')
        return self.click_on_element('VIEW_CART_BUTTON')

    def verify_items_present_in_cart(self, set_with_expected_results):
        self.go_to_cart()
        set_with_actual_results = set(self.fetch_all_cart_items_on_the_page())
        if set_with_expected_results.issubset(set_with_actual_results):
            return True
        else:
            return False
