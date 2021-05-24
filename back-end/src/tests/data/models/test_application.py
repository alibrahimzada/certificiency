import unittest
from src.data.models.event_category import EventCategory
from src.data.models.event import Event
from src.data.models.role import Role
from src.data.models.customer import Customer
from src.data.models.user import User
from src.data.models.application import Application
import datetime

class TestApplication(unittest.TestCase):

    def setUp(self):
        self.event_category = EventCategory()
        self.event = Event()
        self.customer = Customer()
        self.role = Role()
        self.user = User()
        self.application = Application()

        self.event_category.sql_helper.is_test_db = True
        self.event.sql_helper.is_test_db = True
        self.customer.sql_helper.is_test_db = True
        self.role.sql_helper.is_test_db = True
        self.user.sql_helper.is_test_db = True
        self.application.sql_helper.is_test_db = True

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

        # test event_category instances
        self.event_category_data = {
            'event_category_0': { 'event_category_id': 0,
                            'event_category_name': 'Event Category 0'},
            'event_category_1': { 'event_category_id': 1,
                            'event_category_name': 'Event Category 1'}
        }

        # test event instances
        self.event_data = {
            'event_0': { 'event_id': 0,
                        'event_name': 'Event 0',
                        'event_category_id':  self.event_category_data['event_category_0']['event_category_id'],
                        'event_location': "Online",
                        'event_thumbnail': "X",
                        'event_link': "google.com",
                        'event_start_date': datetime.datetime(2021, 6, 6, 17, 0, 0),
                        'event_end_date': datetime.datetime(2021, 6, 6, 18, 0, 0),
                        'event_last_application_date': datetime.datetime(2021, 6, 1, 23, 59, 59),
                        'event_quota': 60,
                        'customer_id': 0
            },
            'event_1': { 'event_id': 1,
                        'event_name': 'Event 1',
                        'event_category_id':  self.event_category_data['event_category_1']['event_category_id'],
                        'event_location': "Online",
                        'event_thumbnail': "X",
                        'event_link': "google.com",
                        'event_start_date': datetime.datetime(2021, 7, 6, 17, 0, 0),
                        'event_end_date': datetime.datetime(2021, 7, 6, 18, 0, 0),
                        'event_last_application_date': datetime.datetime(2021, 7, 1, 23, 59, 59),
                        'event_quota': 100,
                        'customer_id': 1
            }
        }

        # test application instances
        self.application_data = {
            'application_0': { 'application_id': 0,
                        'event_id': self.event_data['event_0']['event_id'],
                        'user_id': self.user_data['user_0']['user_id'],
                        'applied_on': datetime.datetime(2021, 5, 20, 23, 0, 0),
                        'application_status': 1

            },
            'application_1': { 'application_id': 1,
                        'event_id': self.event_data['event_1']['event_id'],
                        'user_id': self.user_data['user_1']['user_id'],
                        'applied_on': datetime.datetime(2021, 5, 20, 23, 0, 0),
                        'application_status': 1 
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

        # the test event categories into test database
        api_response = self.event_category.insert_event_category(self.event_category_data['event_category_0'])
        self.assertEqual(api_response['success'], True)
        api_response = self.event_category.insert_event_category(self.event_category_data['event_category_1'])
        self.assertEqual(api_response['success'], True)

        # inserting the test events into test database
        api_response = self.event.insert_event(self.event_data['event_0'])
        self.assertEqual(api_response['success'], True)
        api_response = self.event.insert_event(self.event_data['event_1'])
        self.assertEqual(api_response['success'], True)

        # inserting the test applications into test database
        api_response = self.application.insert_application(self.application_data['application_0'])
        self.assertEqual(api_response['success'], True)
        api_response = self.application.insert_application(self.application_data['application_1'])
        self.assertEqual(api_response['success'], True)

    def tearDown(self):
        self.remove_test_instance('application_id', self.application_data['application_0']['application_id'], 'applications')
        self.remove_test_instance('application_id', self.application_data['application_1']['application_id'], 'applications')
        self.remove_test_instance('event_id', self.event_data['event_0']['event_id'], 'events')
        self.remove_test_instance('event_id', self.event_data['event_1']['event_id'], 'events')
        self.remove_test_instance('event_category_id', self.event_category_data['event_category_0']['event_category_id'], 'event_categories')
        self.remove_test_instance('event_category_id', self.event_category_data['event_category_1']['event_category_id'], 'event_categories')
        self.remove_test_instance('user_id', self.user_data['user_0']['user_id'], 'users')
        self.remove_test_instance('user_id', self.user_data['user_1']['user_id'], 'users')
        self.remove_test_instance('role_id', self.role_data['role_0']['role_id'], 'roles')
        self.remove_test_instance('role_id', self.role_data['role_1']['role_id'], 'roles')
        self.remove_test_instance('customer_id', self.customer_data['customer_0']['customer_id'], 'customers')
        self.remove_test_instance('customer_id', self.customer_data['customer_1']['customer_id'], 'customers')

    def test_get_all_applications(self):
        # getting all test applications from database
        api_response = self.application.get_all_applications()
        self.assertEqual(api_response['success'], True)

        # asserting every attribute of every application instance
        counter = 0
        for application in self.application_data:
            for key in self.application_data[application]:
                self.assertEqual(self.application_data[application][key], api_response['data'][counter][key])

            counter += 1

    def test_get_application(self):
        # getting the inserted test application from database
        api_response = self.application.get_application(self.application_data['application_0']['application_id'])
        self.assertEqual(api_response['success'], True)


        # asserting every attribute of a application instance
        for key in self.application_data['application_0']:
            self.assertEqual(self.application_data['application_0'][key], api_response['data'][key])



    def test_insert_application(self):
        # getting the inserted test application from database
        api_response = self.application.get_application(self.application_data['application_0']['application_id'])
        self.assertEqual(api_response['success'], True)

        # asserting every attribute of a application instance
        for key in self.application_data['application_0']:
            self.assertEqual(self.application_data['application_0'][key], api_response['data'][key])

        # inserting the same application to test unsuccessful insertion
        api_response = self.application.insert_application(self.application_data['application_0'])
        self.assertEqual(api_response['success'], False)


    def test_delete_application(self):
        # deleting the test application from test database (setting is_deleted attribute = true)
        api_response = self.application.delete_application(self.application_data['application_0'])
        self.assertEqual(api_response['success'], True)

        # getting the deleted test application from database
        api_response = self.application.get_application(self.application_data['application_0']['application_id'])
        self.assertEqual(api_response['success'], True)

        # asserting if is_deleted attribute has been changed to True
        self.assertEqual(api_response['data']['is_deleted'], True)


    def test_update_application(self):
        # updating application attributes
        self.application_data['application_0']['application_status'] = 2
        self.application_data['application_0']['is_deleted'] = False
        api_response = self.application.update_application(self.application_data['application_0'])
        self.assertEqual(api_response['success'], True)

        # getting the updated test application from database
        api_response = self.application.get_application(self.application_data['application_0']['application_id'])
        self.assertEqual(api_response['success'], True)

        self.assertEqual(api_response['data']['application_status'], 2)


    def test_update_application_status(self):
        data = {
            "application_status": 3,
            "application_id": self.application_data['application_0']['application_id']
        }

        api_response = self.application.update_application_status(data)
        self.assertEqual(api_response['success'], True)

        api_response = self.application.get_application(self.application_data['application_0']['application_id'])
        self.assertEqual(api_response['success'], True)

        self.assertEqual(api_response['data']['application_status'], 3)



    def remove_test_instance(self, primary_key_name, primary_key, table_name):
        # removing the test instance from database
        query = """ DELETE FROM {} 
                    WHERE {} = {}
                """.format(table_name, primary_key_name, primary_key)
        self.application.sql_helper.execute(query)