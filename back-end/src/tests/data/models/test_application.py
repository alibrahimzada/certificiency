import unittest
from src.data.models.event import Event
from src.data.models.user import User
from src.data.models.application import Application
from src.data.models.event_category import EventCategory
import datetime

class TestApplication(unittest.TestCase):

    def setUp(self):
        self.application = Application()
        self.event = Event()
        self.user = User()
        self.event_category = EventCategory()
        self.application.sql_helper.is_test_db = True
        self.event.sql_helper.is_test_db = True
        self.user.sql_helper.is_test_db = True
        self.event_category.sql_helper.is_test_db = True

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
                        'event_link': "google.com"
            },
            'event_1': { 'event_id': 1,
                        'event_name': 'Event 1',
                        'event_category_id':  self.event_category_data['event_category_1']['event_category_id'],
                        'event_location': "Online",
                        'event_thumbnail': "X",
                        'event_link': "google.com"
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



        # test application instances
        self.application_data = {
            'application_0': { 'application_id': 0,
                        'event_id': self.event_data['event_0']['event_id'],
                        'user_id': self.user_data['user_0']['user_id'],
                        'applied_on': datetime.datetime(2021, 5, 20, 23, 0, 0),
                        'application_status': 1

            },
            'application_1': { 'application_id': 1,
                        'event_id': self.event_data['event_0']['event_id'],
                        'user_id': self.user_data['user_1']['user_id'],
                        'applied_on': datetime.datetime(2021, 5, 20, 23, 0, 0),
                        'application_status': 1 
            }
        }

    def test_get_all_applications(self):
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

        # inserting the test users into test database
        api_response = self.user.insert_user(self.user_data['user_0'])
        self.assertEqual(api_response['success'], True)
        api_response = self.user.insert_user(self.user_data['user_1'])
        self.assertEqual(api_response['success'], True)


        # inserting the test applications into test database
        api_response = self.application.insert_application(self.application_data['application_0'])
        self.assertEqual(api_response['success'], True)
        api_response = self.application.insert_application(self.application_data['application_1'])
        self.assertEqual(api_response['success'], True)

        # getting all test applications from database
        api_response = self.application.get_all_applications()
        self.assertEqual(api_response['success'], True)

        # asserting every attribute of every application instance
        counter = 0
        for application in self.application_data:
            for key in self.application_data[application]:
                self.assertEqual(self.application_data[application][key], api_response['data'][counter][key])

            self.remove_test_instance(self.application_data[application]['event_category_id'], 'event_categories')
            self.remove_test_instance(self.application_data[application]['event_id'], 'events')
            self.remove_test_instance(self.application_data[application]['user_id'], 'users')
            self.remove_test_instance(self.application_data[application]['application_id'], 'applications')
            counter += 1

    def test_get_application(self):
        # inserting the test event category into test database
        api_response = self.event_category.insert_event_category(self.event_category_data['event_category_0'])
        self.assertEqual(api_response['success'], True)

        # inserting the test event into test database
        api_response = self.event.insert_event(self.event_data['event_0'])
        self.assertEqual(api_response['success'], True)

        # inserting the test user into test database
        api_response = self.user.insert_user(self.user_data['user_0'])
        self.assertEqual(api_response['success'], True)

        # inserting the test application into test database
        api_response = self.application.insert_application(self.application_data['application_0'])
        self.assertEqual(api_response['success'], True)

        # getting the inserted test application from database
        api_response = self.application.get_application(self.application_data['application_0']['application_id'])
        self.assertEqual(api_response['success'], True)


        # asserting every attribute of a application instance
        for key in self.application_data['application_0']:
            self.assertEqual(self.application_data['application_0'][key], api_response['data'][key])

        self.remove_test_instance(self.event_category_data['event_category_0']['event_category_id'], 'event_categories')
        self.remove_test_instance(self.event_data['event_0']['event_id'], 'events')
        self.remove_test_instance(self.user_data['user_0']['user_id'], 'users')
        self.remove_test_instance(self.application_data['application_0']['application_id'], 'applications')

    def test_insert_application(self):
        # inserting the test event category into test database
        api_response = self.event_category.insert_event_category(self.event_category_data['event_category_0'])
        self.assertEqual(api_response['success'], True)

        # inserting the test event into test database
        api_response = self.event.insert_event(self.event_data['event_0'])
        self.assertEqual(api_response['success'], True)

        # inserting the test user into test database
        api_response = self.user.insert_user(self.user_data['user_0'])
        self.assertEqual(api_response['success'], True)

        # inserting the test application into test database
        api_response = self.application.insert_application(self.application_data['application_0'])
        self.assertEqual(api_response['success'], True)

        # getting the inserted test application from database
        api_response = self.application.get_application(self.application_data['application_0']['application_id'])
        self.assertEqual(api_response['success'], True)

        # asserting every attribute of a application instance
        for key in self.application_data['application_0']:
            self.assertEqual(self.application_data['application_0'][key], api_response['data'][key])

        # inserting the same application to test unsuccessful insertion
        api_response = self.application.insert_application(self.application_data['application_0'])
        self.assertEqual(api_response['success'], False)

        self.remove_test_instance(self.event_category_data['event_category_0']['event_category_id'], 'event_categories')
        self.remove_test_instance(self.event_data['event_0']['event_id'], 'events')
        self.remove_test_instance(self.user_data['user_0']['user_id'], 'users')
        self.remove_test_instance(self.application_data['application_0']['application_id'], 'applications')

    def test_delete_application(self):
        # inserting the test event category into test database
        api_response = self.event_category.insert_event_category(self.event_category_data['event_category_0'])
        self.assertEqual(api_response['success'], True)

        # inserting the test event into test database
        api_response = self.event.insert_event(self.event_data['event_0'])
        self.assertEqual(api_response['success'], True)

        # inserting the test user into test database
        api_response = self.user.insert_user(self.user_data['user_0'])
        self.assertEqual(api_response['success'], True)

        # inserting the test application into test database
        api_response = self.application.insert_application(self.application_data['application_0'])
        self.assertEqual(api_response['success'], True)

        data = {'application_id': self.application_data['application_0']['application_id']}

        # deleting the test application from test database (setting is_deleted attribute = true)
        api_response = self.application.delete_application(data)
        self.assertEqual(api_response['success'], True)

        # getting the deleted test application from database
        api_response = self.application.get_application(data['application_id'])
        self.assertEqual(api_response['success'], True)

        # asserting if is_deleted attribute has been changed to True
        self.assertEqual(api_response['data']['is_deleted'], True)

        self.remove_test_instance(self.event_category_data['event_category_0']['event_category_id'], 'event_categories')
        self.remove_test_instance(self.event_data['event_0']['event_id'], 'events')
        self.remove_test_instance(self.user_data['user_0']['user_id'], 'users')
        self.remove_test_instance(self.application_data['application_0']['application_id'], 'applications')

    def test_update_application(self):
        # inserting the test event category into test database
        api_response = self.event_category.insert_event_category(self.event_category_data['event_category_0'])
        self.assertEqual(api_response['success'], True)

        # inserting the test event into test database
        api_response = self.event.insert_event(self.event_data['event_0'])
        self.assertEqual(api_response['success'], True)

        # inserting the test user into test database
        api_response = self.user.insert_user(self.user_data['user_0'])
        self.assertEqual(api_response['success'], True)

        # inserting the test application into test database
        api_response = self.application.insert_application(self.application_data['application_0'])
        self.assertEqual(api_response['success'], True)

        # updating application attributes
        self.application_data['application_0']['application_status'] = 2
        self.application_data['application_0']['is_deleted'] = False
        api_response = self.application.update_application(self.application_data['application_0'])
        self.assertEqual(api_response['success'], True)

        # getting the updated test application from database
        api_response = self.application.get_application(self.application_data['application_0']['application_id'])
        self.assertEqual(api_response['success'], True)

        self.assertEqual(api_response['data']['application_status'], 2)

        self.remove_test_instance(self.event_category_data['event_category_0']['event_category_id'], 'event_categories')
        self.remove_test_instance(self.event_data['event_0']['event_id'], 'events')
        self.remove_test_instance(self.user_data['user_0']['user_id'], 'users')
        self.remove_test_instance(self.application_data['application_0']['application_id'], 'applications')

    def remove_test_instance(self, event_id, table_name):
        # removing the test instance from database
        query = """ DELETE FROM {} 
                    WHERE event_id = {}
                """.format(table_name, event_id)
        self.application.sql_helper.execute(query)
