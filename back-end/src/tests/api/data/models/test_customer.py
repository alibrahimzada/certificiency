import unittest

from src.data.models.customer import Customer

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer = Customer()

    def test_get_all_customers(self):
        pass
