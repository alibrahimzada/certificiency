import sys
import os
sys.path.insert(1, os.getcwd() + '/back-end')

import unittest

from src.tests.data.models.test_customer import TestCustomer
from src.tests.data.models.test_role import TestRole

class TestSuiteRunner():

    def __init__(self):
        self.test_suite = self.create_suite()

    def create_suite(self):
        """
            This method puts all test classes in one place
        """
        test_suite = unittest.TestSuite()
        test_classes = [TestCustomer, TestRole]

        for test_class in test_classes:
            test_suite.addTest(unittest.makeSuite(test_class))

        return test_suite

    def run_tests(self):
        runner = unittest.TextTestRunner()
        runner.run(self.test_suite)

if __name__ == '__main__':
    TestSuiteRunner().run_tests()
