from selenium.webdriver.common.by import By

CURRENCY_CSS_DD = (By.CSS_SELECTOR, '#form-currency > div > button')

CURRENCY_XPATH_DD = (By.XPATH, '//*[@id="form-currency"]/div/button')

CART_TOTAL_CSS_BUTTON = (By.CSS_SELECTOR, '#cart button[data-toggle]')

VIEW_CART_BUTTON = (By.CSS_SELECTOR, '.text-right a[href*="checkout/cart"')

CART_TOTAL_XPATH_BUTTON = (By.XPATH, '//*[@id="cart-total"]')

SEARCH_CSS_FIELD = (By.CSS_SELECTOR, '#search input[name="search"]')

SEARCH_CSS_BUTTON = (By.CSS_SELECTOR, '#search button')

SEARCH_RESULTS_LIST = (By.CSS_SELECTOR, '#content .product-thumb .caption h4')

CART_ITEMS_LIST = (By.CSS_SELECTOR, '.table-responsive .text-left a[href]')

SIZE_CSS_DD = (By.CSS_SELECTOR, '#input-option224')

SIZE_MEDIUM_CSS_OPTION = (By.CSS_SELECTOR, '#input-option224 > option[value="13"]')

SIZE_LARGE_CSS_OPTION = (By.CSS_SELECTOR, '#input-option224 > option[value="14"]')

ADD_TO_CART_CSS_BUTTON = (By.CSS_SELECTOR, '#button-cart')

SIZE_REQUIRED_CSS_WARNING = (By.CSS_SELECTOR, '.text-danger')

CLOSE_ALERT_CSS_BUTTON = (By.CSS_SELECTOR, '.close[data-dismiss="alert"]')
