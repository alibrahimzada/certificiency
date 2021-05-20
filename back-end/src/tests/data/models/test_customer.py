import unittest
from src.data.models.customer import Customer
import datetime

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer = Customer()
        self.customer.sql_helper.is_test_db = True

        # test customer instances
        self.data = {
            'customer_0': { 'customer_id': 0,
                            'customer_name': 'John',
                            'is_active': True,
                            'created_on': datetime.datetime(2009, 5, 5, 18, 33, 45),
                            'company_permissions': "{\"has_update_authorization\": \"False\"}"},
            'customer_1': { 'customer_id': 1,
                            'customer_name': 'Jessica',
                            'is_active': False,
                            'created_on': datetime.datetime(2019, 6, 18, 23, 15, 5),
                            'company_permissions': "{\"has_update_authorization\": \"True\"}"}
        }

    def test_get_all_customers(self):
        # inserting the test customers into test database
        api_response = self.customer.insert_customer(self.data['customer_0'])
        self.assertEqual(api_response['success'], True)
        api_response = self.customer.insert_customer(self.data['customer_1'])
        self.assertEqual(api_response['success'], True)      

        # getting all test customers from database
        api_response = self.customer.get_all_customers()
        self.assertEqual(api_response['success'], True)

        # asserting every attribute of every customer instance
        counter = 0
        for customer in self.data:
            for key in self.data[customer]:
                if key == 'company_permissions':
                    self.assertEqual(eval(self.data[customer][key]), api_response['data'][counter][key])
                    continue

                self.assertEqual(self.data[customer][key], api_response['data'][counter][key])

            self.remove_test_instance(self.data[customer]['customer_id'])
            counter += 1

    def test_get_customer(self):
        # inserting the test customer into test database
        api_response = self.customer.insert_customer(self.data['customer_0'])
        self.assertEqual(api_response['success'], True)

        # getting the inserted test customer from database
        api_response = self.customer.get_customer(self.data['customer_0']['customer_id'])
        self.assertEqual(api_response['success'], True)

        # asserting every attribute of a customer instance
        for key in self.data['customer_0']:
            if key == 'company_permissions':
                self.assertEqual(eval(self.data['customer_0'][key]), api_response['data'][key])
                continue

            self.assertEqual(self.data['customer_0'][key], api_response['data'][key])

        self.remove_test_instance(self.data['customer_0']['customer_id'])

    def test_insert_customer(self):
        # inserting the test customer into test database
        api_response = self.customer.insert_customer(self.data['customer_0'])
        self.assertEqual(api_response['success'], True)

        # getting the inserted test customer from database
        api_response = self.customer.get_customer(self.data['customer_0']['customer_id'])
        self.assertEqual(api_response['success'], True)

        # asserting every attribute of a customer instance
        for key in self.data['customer_0']:
            if key == 'company_permissions':
                self.assertEqual(eval(self.data['customer_0'][key]), api_response['data'][key])
                continue

            self.assertEqual(self.data['customer_0'][key], api_response['data'][key])

        # inserting the same customer to test unsuccessful insertion
        api_response = self.customer.insert_customer(self.data['customer_0'])
        self.assertEqual(api_response['success'], False)

        self.remove_test_instance(self.data['customer_0']['customer_id'])

    def test_delete_customer(self):
        # inserting the test customer into test database
        api_response = self.customer.insert_customer(self.data['customer_0'])
        self.assertEqual(api_response['success'], True)

        data = {'customer_id': self.data['customer_0']['customer_id']}

        # deleting the test customer from test database (setting is_deleted attribute = true)
        api_response = self.customer.delete_customer(data)
        self.assertEqual(api_response['success'], True)

        # getting the deleted test customer from database
        api_response = self.customer.get_customer(data['customer_id'])
        self.assertEqual(api_response['success'], True)

        # asserting if is_deleted attribute has been changed to True
        self.assertEqual(api_response['data']['is_deleted'], True)

        self.remove_test_instance(self.data['customer_0']['customer_id'])

    def test_update_customer(self):
        # inserting the test customer into test database
        api_response = self.customer.insert_customer(self.data['customer_0'])
        self.assertEqual(api_response['success'], True)

        # updating customer attributes
        self.data['customer_0']['customer_name'] = 'Bob'
        self.data['customer_0']['is_deleted'] = False
        api_response = self.customer.update_customer(self.data['customer_0'])
        self.assertEqual(api_response['success'], True)

        # getting the updated test customer from database
        api_response = self.customer.get_customer(self.data['customer_0']['customer_id'])
        self.assertEqual(api_response['success'], True)

        self.assertEqual(api_response['data']['customer_name'], 'Bob')

        self.remove_test_instance(self.data['customer_0']['customer_id'])

    def remove_test_instance(self, customer_id):
        # removing the test instance from database
        query = """ DELETE FROM customers 
                    WHERE customer_id = {}
                """.format(customer_id)
        self.customer.sql_helper.execute(query)
