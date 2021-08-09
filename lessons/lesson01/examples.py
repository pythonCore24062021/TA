import unittest

from func import my_sum


def setUpModule():
    print("setUpModule")


def tearDownModule():
    print("tearDownModule")


class TestRuner(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("\tsetUpClass")

    @classmethod
    def tearDownClass(cls):
        print("\ttearDownClass")


class MySumTests(TestRuner):

    def setUp(self):
        print("\t\tsetUp")
        self.s = my_sum(1, 2, 3, 4)

    def tearDown(self):
        print("\t\ttearDown")

    def test_sum(self):
        print("\t\t\ttest_sum")
        # s = my_sum(1, 2, 3, 4)

        self.assertEqual(self.s, -10)

    def test_sum_eq(self):
        print("\t\t\ttest_sum_eq")
        s = my_sum(1, 2, 3, 4)
        actual = self.s == -10
        self.assertTrue(actual)

    # def test_sum_not_eq(self):
    #     print("\t\t\ttest_sum_not_eq")
    #     s = my_sum(1, 2, 3, 4)
    #     actual = self.s == -10
    #     self.assertFalse(actual)

    def test_sum_not_eq_test(self):
        print("\t\t\ttest_sum_not_eq_test")
        s = my_sum(1, 2, 3, 4)

        actual = not (self.s == -10)
        self.assertFalse(actual)

    def test_list_eq(self):
        print("\t\t\ttest_sum_not_eq_test")
        self.assertListEqual([1, 2, 3, 4], sorted([4, 3, 2, 1]))
        # self.assertEqual([1, 2, 3, 4], [4, 3, 2, 1])


class MySumTests2(TestRuner):

    def setUp(self):
        print("\t\tsetUp")
        self.s = my_sum(1, 2, 3, 4)

    def tearDown(self):
        print("\t\ttearDown")

    def test_sum(self):
        print("\t\t\ttest_sum")
        # s = my_sum(1, 2, 3, 4)

        self.assertEqual(self.s, -10)

    def test_sum_eq(self):
        print("\t\t\ttest_sum_eq")
        s = my_sum(1, 2, 3, 4)
        actual = self.s == -10
        self.assertTrue(actual)

    # def test_sum_not_eq(self):
    #     print("\t\t\ttest_sum_not_eq")
    #     s = my_sum(1, 2, 3, 4)
    #     actual = self.s == -10
    #     self.assertFalse(actual)

    def test_sum_not_eq_test(self):
        print("\t\t\ttest_sum_not_eq_test")
        s = my_sum(1, 2, 3, 4)

        actual = not (self.s == -10)
        self.assertFalse(actual)

    def test_list_eq(self):
        print("\t\t\ttest_sum_not_eq_test")
        self.assertListEqual([1, 2, 3, 4], sorted([4, 3, 2, 1]))
        # self.assertEqual([1, 2, 3, 4], [4, 3, 2, 1])


# print("ex: ", __name__)

if __name__ == "__main__":
    unittest.main()
