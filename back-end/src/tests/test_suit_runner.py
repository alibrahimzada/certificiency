import sys
import os
sys.path.insert(1, os.getcwd() + '/back-end')

import unittest

from src.tests.data.models.test_customer import TestCustomer
from src.tests.data.models.test_role import TestRole
from src.tests.data.models.test_user import TestUser
from src.tests.data.models.test_event_category import TestEventCategory
from src.tests.data.models.test_event import TestEvent
from src.tests.data.models.test_application import TestApplication
from src.tests.data.models.test_certificate import TestCertificate
from src.tests.data.models.test_auth import TestAuth

class TestSuiteRunner():

    def __init__(self):
        self.test_suite = self.create_suite()

    def create_suite(self):
        """
            This method puts all test classes in one place
        """
        test_suite = unittest.TestSuite()
        test_classes = [TestCustomer, TestRole, TestUser, TestEventCategory,
                        TestEvent, TestApplication, TestCertificate, TestAuth]

        for test_class in test_classes:
            test_suite.addTest(unittest.makeSuite(test_class))

        return test_suite

    def run_tests(self):
        runner = unittest.TextTestRunner()
        runner.run(self.test_suite)

if __name__ == '__main__':
    TestSuiteRunner().run_tests()
