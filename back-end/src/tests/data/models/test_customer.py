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
                            'customer_name': 'Turkcell',
                            'is_active': True,
                            'created_on': datetime.datetime(2009, 5, 5, 18, 33, 45),
                            'company_permissions': "{\"can_create_multiple_events\": \"False\"}",
                            'domain_name': 'turkcell.com'},
            'customer_1': { 'customer_id': 1,
                            'customer_name': 'Vodafone',
                            'is_active': False,
                            'created_on': datetime.datetime(2019, 6, 18, 23, 15, 5),
                            'company_permissions': "{\"can_create_multiple_events\": \"True\"}",
                            'domain_name': 'vodafone.com'}
        }

        # inserting the test customers into test database
        api_response = self.customer.insert_customer(self.data['customer_0'])
        self.assertEqual(api_response['success'], True)
        api_response = self.customer.insert_customer(self.data['customer_1'])
        self.assertEqual(api_response['success'], True)


    def tearDown(self):
        self.remove_test_instance(self.data['customer_0']['customer_id'])
        self.remove_test_instance(self.data['customer_1']['customer_id'])


    def test_get_all_customers(self):
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

            counter += 1


    def test_get_customer(self):
        # getting the inserted test customer from database
        api_response = self.customer.get_customer(self.data['customer_0']['customer_id'])
        self.assertEqual(api_response['success'], True)

        # asserting every attribute of a customer instance
        for key in self.data['customer_0']:
            if key == 'company_permissions':
                self.assertEqual(eval(self.data['customer_0'][key]), api_response['data'][key])
                continue

            self.assertEqual(self.data['customer_0'][key], api_response['data'][key])


    def test_insert_customer(self):
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


    def test_delete_customer(self):
        # deleting the test customer from test database (setting is_deleted attribute = true)
        api_response = self.customer.delete_customer(self.data['customer_0'])
        self.assertEqual(api_response['success'], True)

        # getting the deleted test customer from database
        api_response = self.customer.get_customer(self.data['customer_0']['customer_id'])
        self.assertEqual(api_response['success'], True)

        # asserting if is_deleted attribute has been changed to True
        self.assertEqual(api_response['data']['is_deleted'], True)


    def test_update_customer(self):
        # updating customer attributes
        self.data['customer_0']['customer_name'] = 'TurkTelekom'
        self.data['customer_0']['is_deleted'] = False
        api_response = self.customer.update_customer(self.data['customer_0'])
        self.assertEqual(api_response['success'], True)

        # getting the updated test customer from database
        api_response = self.customer.get_customer(self.data['customer_0']['customer_id'])
        self.assertEqual(api_response['success'], True)

        self.assertEqual(api_response['data']['customer_name'], 'TurkTelekom')


    def test_make_active(self): 
        api_response = self.customer.make_active(self.data['customer_0']['customer_id'])
        self.assertEqual(api_response['success'], True)

        # getting the test customer from database
        api_response = self.customer.get_customer(self.data['customer_0']['customer_id'])
        self.assertEqual(api_response['success'], True)

        self.assertEqual(api_response['data']['is_active'], True)


    def test_make_passive(self): 
        api_response = self.customer.make_passive(self.data['customer_0']['customer_id'])
        self.assertEqual(api_response['success'], True)

        # getting the test customer from database
        api_response = self.customer.get_customer(self.data['customer_0']['customer_id'])
        self.assertEqual(api_response['success'], True)

        self.assertEqual(api_response['data']['is_active'], False)


    def remove_test_instance(self, primary_key):
        # removing the test instance from database
        query = """ DELETE FROM customers 
                    WHERE customer_id = {}
                """.format(primary_key)
        self.customer.sql_helper.execute(query)
