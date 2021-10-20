import os
import sys, getopt
abspath = os.path.abspath(__file__)
root = os.path.dirname(os.path.dirname(abspath))
sys.path.append(root)

import time
import unittest

from selenium import webdriver

from Register.pages.home import Home

# desired_capabilities ={
#     'browserName': 'chrome'
# }
class RegisterPage(unittest.TestCase):
    driver = None

    def setUp(self):
        self.driver.get("http://taqc-opencart.epizy.com/")
        time.sleep(1)
        self.home = Home(self.driver)

    def tearDown(self):
        time.sleep(2)

    @classmethod
    def setUpClass(cls):
        desired_capabilities = {
            'browserName': 'firefox'
        }
        cls.driver = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            desired_capabilities=desired_capabilities
        )
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_first_reg_user(self):
        register_page = self.home.get_header()\
            .account_dropdown\
            .click()\
            .clickRegister() \
            .set_firstname("Popandopalo2") \
            .set_lastname("Test2") \
            .set_email(f"rul+{int(time.time())}@gmail.com") \
            .set_telephone("55555") \
            .set_address("street") \
            .set_city("Lviv") \
            .set_postcode("79000") \
            .set_country("Ukraine") \
            .set_region("Kyiv") \
            .set_password("789456") \
            .set_passwordconfirm("789456") \
            .set_privacycheckmark() \
 \
            .click_continue()

        self.assertEqual(register_page.get_successmessage().get_message(), 'Your Account Has Been Created!')
#
#
# def main(argv):
#     global desired_capabilities
#     try:
#         opts, args = getopt.getopt(argv, "hc:f", ["chrome=","firefox="])
#     except getopt.GetoptError:
#         print("test.py -c <True/False> -f <True/False>")
#     for opt, arg in opts:
#         print(opt, arg)
#         if opt in ("-c", "--chrome"):
#             desired_capabilities = {
#                 'browserName': 'chrome'
#             }
#
#         if opt in ("-f", "--firefox"):
#             desired_capabilities = {
#                 'browserName': 'firefox'
#             }
#     unittest.main()
#
# if __name__ == "__main__":
#     main(sys.argv[1:])

