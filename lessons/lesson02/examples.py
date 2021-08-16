import time
import sys
import pprint

from selenium.webdriver.common.keys import Keys

pprint.pprint(sys.path)
from selenium import webdriver
driver = webdriver.Chrome()

driver.get("https://www.python.org/")

element = driver.find_element_by_id("id-search-field")
element.send_keys("py")
time.sleep(2)
element = driver.find_element_by_name("q")
element.send_keys("python")
time.sleep(2)
element = driver.find_element_by_css_selector("#id-search-field")
element.send_keys("pyTest")
time.sleep(2)
element = driver.find_element_by_xpath('//*[@id="id-search-field"]')
element.send_keys("py")
time.sleep(2)

# element.send_keys(Keys.)
driver.back()

# b = driver.find_element_by_css_selector('#submit')
# b.click()

time.sleep(5)

driver.quit()

# driver = webdriver.Firefox()
#
# driver.get("https://google.com")
# time.sleep(2)
#
#
# driver.quit()
# driver.close()
