#Please, write integration tests by Selenium WebDriver to verify some features of Open Cart Application.
#Please develop next methods in the FirstSeleniumTest class

#checkAddToCart method - to check the functionality of adding items 'Xiaomi Mi 8' and 'MacBook' to cart.


def checkCurrencyChange(self):
    currency_btm = self.driver.find_element_by_css_selector(
        "#form-currency > div > button > span"
    )
    currency_btm.click()
    eur_btn = self.driver.find_element_by_css_selector(
        "#form-currency > div > ul > li:nth-child(1) > button")
    eur_btn.click()

    search_input = self.driver.find_elements_by_xpath('.//div[2]/div[1]/div/div[2]/p[2]').text
    search_input.send_keys("€")