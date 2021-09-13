class BaseElement:
    def __init__(self, driver, locators):
        self.driver = driver
        self.locator = locators
        self.element = self.driver.find_element(*self.locator)
