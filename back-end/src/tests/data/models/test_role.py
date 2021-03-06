import unittest
from src.data.models.role import Role
from src.data.models.customer import Customer
import datetime

class TestRole(unittest.TestCase):

    def setUp(self):
        self.role = Role()
        self.customer = Customer()
        self.role.sql_helper.is_test_db = True
        self.customer.sql_helper.is_test_db = True

        # test customer instances
        self.customer_data = {
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

        # test role instances
        self.role_data = {
            'role_0': { 'role_id': 0,
                        'role_name': 'admin',
                        'role_permissions': "{\"has_delete_authorization\": \"True\"}",
                        'customer_id': self.customer_data['customer_0']['customer_id']
            },
            'role_1': { 'role_id': 1,
                        'role_name': 'client',
                        'role_permissions': "{\"has_delete_authorization\": \"False\"}",
                        'customer_id': self.customer_data['customer_1']['customer_id']
            }

        }

        # inserting the test customers into test database
        api_response = self.customer.insert_customer(self.customer_data['customer_0'])
        self.assertEqual(api_response['success'], True)
        api_response = self.customer.insert_customer(self.customer_data['customer_1'])
        self.assertEqual(api_response['success'], True)

        # inserting the test roles into test database
        api_response = self.role.insert_role(self.role_data['role_0'])
        self.assertEqual(api_response['success'], True)
        api_response = self.role.insert_role(self.role_data['role_1'])
        self.assertEqual(api_response['success'], True)


    def tearDown(self):
        self.remove_test_instance('role_id', self.role_data['role_0']['role_id'], 'roles')
        self.remove_test_instance('role_id', self.role_data['role_1']['role_id'], 'roles')
        self.remove_test_instance('customer_id', self.customer_data['customer_0']['customer_id'], 'customers')
        self.remove_test_instance('customer_id', self.customer_data['customer_1']['customer_id'], 'customers')

    def test_get_all_roles(self):
        # getting all test roles from database
        api_response = self.role.get_all_roles()
        self.assertEqual(api_response['success'], True)

        # asserting every attribute of every role instance
        counter = 0
        for role in self.role_data:
            for key in self.role_data[role]:
                if key == 'role_permissions':
                    self.assertEqual(eval(self.role_data[role][key]), api_response['data'][counter][key])
                    continue

                self.assertEqual(self.role_data[role][key], api_response['data'][counter][key])

            counter += 1

    def test_get_role(self):
        # getting the inserted test role from database
        api_response = self.role.get_role(self.role_data['role_0']['role_id'])
        self.assertEqual(api_response['success'], True)

        # asserting every attribute of a role instance
        for key in self.role_data['role_0']:
            if key == 'role_permissions':
                self.assertEqual(eval(self.role_data['role_0'][key]), api_response['data'][key])
                continue

            self.assertEqual(self.role_data['role_0'][key], api_response['data'][key])

    def test_insert_role(self):
        # getting the inserted test role from database
        api_response = self.role.get_role(self.role_data['role_0']['role_id'])
        self.assertEqual(api_response['success'], True)

        # asserting every attribute of a role instance
        for key in self.role_data['role_0']:
            if key == 'role_permissions':
                self.assertEqual(eval(self.role_data['role_0'][key]), api_response['data'][key])
                continue

            self.assertEqual(self.role_data['role_0'][key], api_response['data'][key])

        # inserting the same role to test unsuccessful insertion
        api_response = self.role.insert_role(self.role_data['role_0'])
        self.assertEqual(api_response['success'], False)

    def test_delete_role(self):
        # deleting the test role from test database (setting is_deleted attribute = true)
        api_response = self.role.delete_role(self.role_data['role_0'])
        self.assertEqual(api_response['success'], True)

        # getting the deleted test role from database
        api_response = self.role.get_role(self.role_data['role_0']['role_id'])
        self.assertEqual(api_response['success'], True)

        # asserting if is_deleted attribute has been changed to True
        self.assertEqual(api_response['data']['is_deleted'], True)

    def test_update_role(self):
        # updating role attributes
        self.role_data['role_0']['role_name'] = 'Analyst'
        self.role_data['role_0']['is_deleted'] = False
        api_response = self.role.update_role(self.role_data['role_0'])
        self.assertEqual(api_response['success'], True)

        # getting the updated test role from database
        api_response = self.role.get_role(self.role_data['role_0']['role_id'])
        self.assertEqual(api_response['success'], True)

        self.assertEqual(api_response['data']['role_name'], 'Analyst')

    def remove_test_instance(self, primary_key_name, primary_key, table_name):
        # removing the test instance from database
        query = """ DELETE FROM {} 
                    WHERE {} = {}
                """.format(table_name, primary_key_name, primary_key)
        self.role.sql_helper.execute(query)
