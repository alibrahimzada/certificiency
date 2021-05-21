import unittest
from src.data.models.event import Event
from src.data.models.event_category import EventCategory
import datetime

class TestEvent(unittest.TestCase):

    def setUp(self):
        self.event = Event()
        self.event_category = EventCategory()
        self.event.sql_helper.is_test_db = True
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

        # inserting the test event_categorys into test database
        api_response = self.event_category.insert_event_category(self.event_category_data['event_category_0'])
        self.assertEqual(api_response['success'], True)
        api_response = self.event_category.insert_event_category(self.event_category_data['event_category_1'])
        self.assertEqual(api_response['success'], True)

        # inserting the test events into test database
        api_response = self.event.insert_event(self.event_data['event_0'])
        self.assertEqual(api_response['success'], True)
        api_response = self.event.insert_event(self.event_data['event_1'])
        self.assertEqual(api_response['success'], True)


    def tearDown(self):
        self.remove_test_instance('event_id', self.event_data['event_0']['event_id'], 'events')
        self.remove_test_instance('event_id', self.event_data['event_1']['event_id'], 'events')
        self.remove_test_instance('event_category_id', self.event_category_data['event_category_0']['event_category_id'], 'event_categories')
        self.remove_test_instance('event_category_id', self.event_category_data['event_category_1']['event_category_id'], 'event_categories')


    def test_get_all_events(self):
        # getting all test events from database
        api_response = self.event.get_all_events()
        self.assertEqual(api_response['success'], True)

        # asserting every attribute of every event instance
        counter = 0
        for event in self.event_data:
            for key in self.event_data[event]:
                self.assertEqual(self.event_data[event][key], api_response['data'][counter][key])
        
            counter += 1

    def test_get_event(self):
        # getting the inserted test event from database
        api_response = self.event.get_event(self.event_data['event_0']['event_id'])
        self.assertEqual(api_response['success'], True)

        # asserting every attribute of a event instance
        for key in self.event_data['event_0']:
            self.assertEqual(self.event_data['event_0'][key], api_response['data'][key])




    def test_insert_event(self):
        # getting the inserted test event from database
        api_response = self.event.get_event(self.event_data['event_0']['event_id'])
        self.assertEqual(api_response['success'], True)

        # asserting every attribute of a event instance
        for key in self.event_data['event_0']:
            self.assertEqual(self.event_data['event_0'][key], api_response['data'][key])

        # inserting the same event to test unsuccessful insertion
        api_response = self.event.insert_event(self.event_data['event_0'])
        self.assertEqual(api_response['success'], False)



    def test_delete_event(self):
        # deleting the test event from test database (setting is_deleted attribute = true)
        api_response = self.event.delete_event(self.event_data['event_0'])
        self.assertEqual(api_response['success'], True)

        # getting the deleted test event from database
        api_response = self.event.get_event(self.event_data['event_0']['event_id'])
        self.assertEqual(api_response['success'], True)

        # asserting if is_deleted attribute has been changed to True
        self.assertEqual(api_response['data']['is_deleted'], True)



    def test_update_event(self):
        # updating event attributes
        self.event_data['event_0']['event_name'] = 'Updated Event 0'
        self.event_data['event_0']['is_deleted'] = False

        api_response = self.event.update_event(self.event_data['event_0'])
        self.assertEqual(api_response['success'], True)

        # getting the updated test event from database
        api_response = self.event.get_event(self.event_data['event_0']['event_id'])
        self.assertEqual(api_response['success'], True)

        self.assertEqual(api_response['data']['event_name'], 'Updated Event 0')


    def remove_test_instance(self, primary_key_name, primary_key, table_name):
        # removing the test instance from database
        query = """ DELETE FROM {} 
                    WHERE {} = {}
                """.format(table_name, primary_key_name, primary_key)
        self.event.sql_helper.execute(query)

