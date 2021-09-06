# from HW.achornyi.TASolution.Framework.Web import drivers
import json

from HW.achornyi.TASolution.Framework.Web import drivers
from HW.achornyi.TASolution.Tests.TestCases.BaseTestCase import BaseTestCase


class HW02Tests(BaseTestCase):
    def setUp(self):
        drivers.current.get("http://taqc-opencart.epizy.com/")

    def tearDown(self):
        pass

    def test_hw02_task01(self):
        pass
