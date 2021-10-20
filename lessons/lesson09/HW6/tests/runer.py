import getopt
import sys
import unittest

import test_register_user_gread
import test_register_user_gread_f

# suite = unittest.TestLoader().loadTestsFromModule(test_register_user_gread)
# unittest.TextTestRunner(verbosity=2).run(suite)


def main(argv):
    try:
        opts, args = getopt.getopt(argv, "hc:f", ["chrome=", "firefox="])
    except getopt.GetoptError:
        print("test.py -c <True/False> -f <True/False>")
    for opt, arg in opts:
        print(opt, arg)
        if opt in ("-c", "--chrome"):
            suite = unittest.TestLoader().loadTestsFromModule(test_register_user_gread)
            unittest.TextTestRunner(verbosity=2).run(suite)

        if opt in ("-f", "--firefox"):
            suite = unittest.TestLoader().loadTestsFromTestCase(test_register_user_gread_f.RegisterPage)
            unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    print(sys.argv)
    main(sys.argv[1:])



