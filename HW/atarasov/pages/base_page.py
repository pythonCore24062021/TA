import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from HW.atarasov.data.constants import TIMEOUT, TIMEOUT_SHORT
from HW.atarasov.pages import locators


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def wait_until_page_is_loaded(self, url, timeout=1):
        start = time.time()
        while not self.page_has_loaded(url):
            if time.time() - start >= timeout:
                raise TimeoutError('Page was not loaded in time ')

    def get_url(self):
        return self.driver.current_url

    @staticmethod
    def is_url_changed(url):
        if expected_conditions.url_changes(url):
            return True
        else:
            return False

    def return_back(self):
        return self.driver.back()

    def get_element(self, locators, wait_type=expected_conditions.presence_of_element_located, timeout=TIMEOUT):
        WebDriverWait(self.driver, timeout).until(wait_type(locators))
        return self.driver.find_element(*locators)

    def get_elements(self, locators, wait_type=expected_conditions.presence_of_all_elements_located, timeout=TIMEOUT,
                     elem=None):
        if elem is None:
            WebDriverWait(self.driver, timeout).until(wait_type(locators))
            return self.driver.find_elements(*locators)
        return elem.find_elements(*locators)

    def javascript(self, command):
        return self.driver.execute_script(command)

    def page_has_loaded(self, url):
        current_url = self.get_url()
        page_state = self.javascript('return document.readyState;')
        return page_state == 'complete' and url in current_url

    def navigate_to_url(self, url):
        return self.driver.get(url)

    def check_element_is_enabled(self, loc, timeout):
        return self.get_element(getattr(locators, loc), timeout=timeout).is_enabled()

    def click_on_element(self, element, loc=False):
        if loc:
            self.get_element(element).click()
        else:
            self.get_element(getattr(locators, element)).click()
        return True

    def get_text_of_element(self, element):
        element = self.get_element(getattr(locators, element))
        return element.text

    def get_text_of_elements(self, elements):
        elements = self.get_elements(getattr(locators, elements))
        return [i.text for i in elements]

    def enter_input_to_field(self, element, text):
        return self.get_element(getattr(locators, element)).send_keys(text)

    def get_a_list_with_elements(self, element):
        return self.get_elements(getattr(locators, element))

    @staticmethod
    def create_dynamic_locator(start_string, option):
        locator = start_string + option + '\']'
        return locator

    def get_value_in_dropdown_using_xpath(self, option):
        start_string = """//*[@class="dropdown-menu"]//button[text()='"""
        return By.XPATH, self.create_dynamic_locator(start_string, option)

    def get_value_in_dropdown_using_css(self, option):
        start_string = """.dropdown-menu button[name='"""
        return By.CSS_SELECTOR, self.create_dynamic_locator(start_string, option)

    def get_specific_search_result_element(self, item_name):
        start_string = """//*[@class="caption"]//a[text()='"""
        return By.XPATH, self.create_dynamic_locator(start_string, item_name)



