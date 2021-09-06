#
# def f(a,b,c, *args):
#     print(f"{a=} {b=} {c=} {args=}")
# l = (1,2,3, 3,4,5,6,7,8,8,)
#
# f(l[0], l[1], l[2])
# f(*l)
#
# d = {"a":"a", "b":"b", "c":"c" }
# f(**d)
# f(b=d['b'], a=d['a'],c=d['c'])

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://www.google.com")
searchElement = driver.find_element(By.NAME, "q")
searchElement = driver.find_element_by_name("q")
searchElement.send_keys("Selenium download")
searchElement.submit()
wait = WebDriverWait(driver, 5)


class Element_has_text:
    def __init__(self, locator, text):
        self.locator = locator
        self.text = text

    def __call__(self, driver):
        element = driver.find_element(*self.locator)

        if self.text in driver.page_source:
            return element
        else:
            return False


element = wait.until(Element_has_text((By.CSS_SELECTOR, "#rso > div:nth-child(1) > div > div > div.yuRUbf > a > h3"),
                                      "Downloads | Selenium"))
element.click()

# driver.implicitly_wait(5)
# driver.find_element(By.LINK_TEXT, "Downloads - Selenium").click()      # Error
