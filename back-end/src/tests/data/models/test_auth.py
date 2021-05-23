import unittest
from src.data.models.customer import Customer
from src.data.models.user import User
from src.data.models.role import Role
from src.data.models.auth import Auth
import datetime

class TestAuth(unittest.TestCase):

    def setUp(self):
        self.auth = Auth()
        self.user = User()
        self.role = Role()
        self.customer = Customer()
        self.auth.sql_helper.is_test_db = True
        self.user.sql_helper.is_test_db = True
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

        # test user instances
        self.user_data = {
            'user_0': { 'user_id': 0,
                        'username': 'John',
                        'password': 'Elongated Musk',
                        'first_name': 'John',
                        'last_name': 'Cena',
                        'customer_id': 0,
                        'role_id': 0,
                        'is_active': True,
                        'email': 'johncena@gmail.com',
                        'created_on': datetime.datetime(2021, 5, 20, 21, 15, 30),
                        'last_login': datetime.datetime(2021, 5, 20, 22, 0, 0)
            },
            'user_1': { 'user_id': 1,
                        'username': 'Jessica',
                        'password': 'I am Jessica',
                        'first_name': 'Jessica',
                        'last_name': 'Johnes',
                        'customer_id': 1,
                        'role_id': 1,
                        'is_active': True,
                        'email': 'jj11@gmail.com',
                        'created_on': datetime.datetime(2021, 5, 20, 21, 18, 45),
                        'last_login': datetime.datetime(2021, 5, 20, 23, 0, 0)
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

        # inserting the test users into test database
        api_response = self.user.insert_user(self.user_data['user_0'])
        self.assertEqual(api_response['success'], True)
        api_response = self.user.insert_user(self.user_data['user_1'])
        self.assertEqual(api_response['success'], True)

    def tearDown(self):
        self.remove_test_instance('user_id', self.user_data['user_0']['user_id'], 'users')
        self.remove_test_instance('user_id', self.user_data['user_1']['user_id'], 'users')
        self.remove_test_instance('role_id', self.role_data['role_0']['role_id'], 'roles')
        self.remove_test_instance('role_id', self.role_data['role_1']['role_id'], 'roles')
        self.remove_test_instance('customer_id', self.customer_data['customer_0']['customer_id'], 'customers')
        self.remove_test_instance('customer_id', self.customer_data['customer_1']['customer_id'], 'customers')

    def test_login(self):
        data_1 = {'username': 'John', 'password': 'Elongated Musk'}
        data_2 = {'username': 'unavailable user', 'password': 'xxx'}

        api_response = self.auth.login(data_1)
        self.assertEqual(api_response['success'], True)

        for key in self.user_data['user_0']:
            self.assertEqual(self.user_data['user_0'][key], api_response['data'][key])

        api_response = self.auth.login(data_2)
        self.assertEqual(api_response['success'], False)

    def remove_test_instance(self, primary_key_name, primary_key, table_name):
        # removing the test instance from database
        query = """ DELETE FROM {} 
                    WHERE {} = {}
                """.format(table_name, primary_key_name, primary_key)
        self.role.sql_helper.execute(query)
