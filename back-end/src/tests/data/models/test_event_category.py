import unittest
from src.data.models.event_category import EventCategory

class TestEventCategory(unittest.TestCase):

    def setUp(self):
        self.event_category = EventCategory()
        self.event_category.sql_helper.is_test_db = True

        # test event_category instances
        self.data = {
            'event_category_0': { 'event_category_id': 0,
                            'event_category_name': 'Event Category 0'},
            'event_category_1': { 'event_category_id': 1,
                            'event_category_name': 'Event Category 1'}
                          
        }


        # inserting the test event_categories into test database
        api_response = self.event_category.insert_event_category(self.data['event_category_0'])
        self.assertEqual(api_response['success'], True)
        api_response = self.event_category.insert_event_category(self.data['event_category_1'])
        self.assertEqual(api_response['success'], True)     


    def tearDown(self):
        self.remove_test_instance(self.data['event_category_0']['event_category_id'])
        self.remove_test_instance(self.data['event_category_1']['event_category_id'])        



    def test_get_all_event_categories(self):
        # getting all test event_categorys from database
        api_response = self.event_category.get_all_event_categories()
        self.assertEqual(api_response['success'], True)

        # asserting every attribute of every event_category instance
        counter = 0
        for event_category in self.data:
            for key in self.data[event_category]:  
                self.assertEqual(self.data[event_category][key], api_response['data'][counter][key])

            counter += 1

    def test_get_event_category(self):
        # getting the inserted test event_category from database
        api_response = self.event_category.get_event_category(self.data['event_category_0']['event_category_id'])
        self.assertEqual(api_response['success'], True)

        # asserting every attribute of a event_category instance
        for key in self.data['event_category_0']:
            self.assertEqual(self.data['event_category_0'][key], api_response['data'][key])



    def test_insert_event_category(self):
        # getting the inserted test event_category from database
        api_response = self.event_category.get_event_category(self.data['event_category_0']['event_category_id'])
        self.assertEqual(api_response['success'], True)

        # asserting every attribute of a event_category instance
        for key in self.data['event_category_0']:
            self.assertEqual(self.data['event_category_0'][key], api_response['data'][key])

        # inserting the same event_category to test unsuccessful insertion
        api_response = self.event_category.insert_event_category(self.data['event_category_0'])
        self.assertEqual(api_response['success'], False)


    def test_delete_event_category(self):

        # deleting the test event_category from test database (setting is_deleted attribute = true)
        api_response = self.event_category.delete_event_category(self.data['event_category_0'])
        self.assertEqual(api_response['success'], True)

        # getting the deleted test event_category from database
        api_response = self.event_category.get_event_category(self.data['event_category_0']['event_category_id'])
        self.assertEqual(api_response['success'], True)

        # asserting if is_deleted attribute has been changed to True
        self.assertEqual(api_response['data']['is_deleted'], True)


    def test_update_event_category(self):
        # updating event_category attributes
        self.data['event_category_0']['event_category_name'] = 'Updated Event Category 0'
        self.data['event_category_0']['is_deleted'] = False
        api_response = self.event_category.update_event_category(self.data['event_category_0'])
        self.assertEqual(api_response['success'], True)

        # getting the updated test event_category from database
        api_response = self.event_category.get_event_category(self.data['event_category_0']['event_category_id'])
        self.assertEqual(api_response['success'], True)

        self.assertEqual(api_response['data']['event_category_name'], 'Updated Event Category 0')


    def remove_test_instance(self, event_category_id):
        # removing the test instance from database
        query = """ DELETE FROM event_categories 
                    WHERE event_category_id = {}
                """.format(event_category_id)
        self.event_category.sql_helper.execute(query)
