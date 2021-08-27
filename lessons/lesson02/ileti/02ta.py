import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.python.org/")
element = driver.find_element_by_id("id-search-field")
element.send_keys("i code with python")
time.sleep(2)
element = driver.find_element_by_xpath('//*[@id="id-search-field"]')
element.send_keys(" and selenium")
element.send_keys(Keys.ENTER)
time.sleep(2)
driver.back()
element = driver.find_element_by_xpath('//*[@id="id-search-field"]')
element.send_keys(" and selenium2")
b = driver.find_element_by_css_selector("#submit")
b.click()
time.sleep(5)


driver.quit()

# driver = webdriver.Firefox()
# driver.get("https:google.com")
# time.sleep(2)
# driver.quit()