import unittest
from src.data.models.role import Role
from src.data.models.customer import Customer
from src.data.models.user import User
import datetime

class TestUser(unittest.TestCase):

    def setUp(self):
        self.user = User()
        self.role = Role()
        self.customer = Customer()
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

    def test_get_all_users(self):
        # getting all test users from database
        api_response = self.user.get_all_users()
        self.assertEqual(api_response['success'], True)

        # asserting every attribute of every user instance
        counter = 0
        for user in self.user_data:
            for key in self.user_data[user]:
                self.assertEqual(self.user_data[user][key], api_response['data'][counter][key])

            counter += 1

    def test_get_user(self):
        # getting the inserted test user from database
        api_response = self.user.get_user(self.user_data['user_0']['user_id'])
        self.assertEqual(api_response['success'], True)

        # asserting every attribute of a user instance
        for key in self.user_data['user_0']:
            self.assertEqual(self.user_data['user_0'][key], api_response['data'][key])

    def test_insert_user(self):
        # getting the inserted test user from database
        api_response = self.user.get_user(self.user_data['user_0']['user_id'])
        self.assertEqual(api_response['success'], True)

        # asserting every attribute of a user instance
        for key in self.user_data['user_0']:
            self.assertEqual(self.user_data['user_0'][key], api_response['data'][key])

        # inserting the same user to test unsuccessful insertion
        api_response = self.user.insert_user(self.user_data['user_0'])
        self.assertEqual(api_response['success'], False)

    def test_delete_user(self):
        # deleting the test user from test database (setting is_deleted attribute = true)
        api_response = self.user.delete_user(self.user_data['user_0'])
        self.assertEqual(api_response['success'], True)

        # getting the deleted test user from database
        api_response = self.user.get_user(self.user_data['user_0']['user_id'])
        self.assertEqual(api_response['success'], True)

        # asserting if is_deleted attribute has been changed to True
        self.assertEqual(api_response['data']['is_deleted'], True)

    def test_update_user(self):
        # updating role attributes
        self.user_data['user_0']['username'] = 'Jack'
        self.user_data['user_0']['is_deleted'] = False
        api_response = self.user.update_user(self.user_data['user_0'])
        self.assertEqual(api_response['success'], True)

        # getting the updated test user from database
        api_response = self.user.get_user(self.user_data['user_0']['user_id'])
        self.assertEqual(api_response['success'], True)

        self.assertEqual(api_response['data']['username'], 'Jack')

    def remove_test_instance(self, primary_key_name, primary_key, table_name):
        # removing the test instance from database
        query = """ DELETE FROM {} 
                    WHERE {} = {}
                """.format(table_name, primary_key_name, primary_key)
        self.role.sql_helper.execute(query)
