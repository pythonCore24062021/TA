import unittest
from HW.achornyi.ta_solution.framework.web import drivers

from selenium import webdriver


class BaseTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        drivers.current = webdriver.Chrome()
        drivers.current.maximize_window()

    @classmethod
    def tearDownClass(cls):
        drivers.current.quit()
