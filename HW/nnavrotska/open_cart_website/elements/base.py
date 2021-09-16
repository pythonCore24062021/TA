class BaseElement:
    def __init__(self, driver, locators):
        self.driver = driver
        self.locators = locators
        self.element = self.driver.find_element(*self.locators)
