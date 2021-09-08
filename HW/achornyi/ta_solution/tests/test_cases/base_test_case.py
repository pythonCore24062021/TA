import unittest
from HW.achornyi.ta_solution.framework.web import drivers

from selenium import webdriver

from HW.achornyi.ta_solution.tests.repositories import base_repository
from ui.pages.home_page import HomePage


class BaseTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        drivers.current = webdriver.Chrome()
        drivers.current.maximize_window()

    @classmethod
    def tearDownClass(cls):
        drivers.current.quit()

    def setUp(self):
        drivers.current.get(base_repository.BASE_URL)
        home_page = HomePage()
