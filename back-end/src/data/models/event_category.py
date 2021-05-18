from src.data.models.base_entity import BaseEntity
from psycopg2.errors import UniqueViolation

class EventCategory(BaseEntity):
    def __init__(self):
        super(EventCategory, self).__init__()
  
    def get_all_event_categories(self):
        api_response = {'status': 200, 'success': True, 'errors': []}
        rows = self.sql_helper.get_rows('event_categories')
        api_response['data'] = rows
        return api_response

    def get_event_category(self, event_category_id):
        api_response = {'status': 200, 'success': True, 'errors': []}
        event_category_data = self.sql_helper.get_single_instance('event_categories', 'event_category_id', event_category_id)
        api_response['data'] = event_category_data
        return api_response

    def insert_event_category(self, data):
        query = """INSERT INTO \"event_categories\"
                   values({}, '{}', '{}');
                   """.format(data['event_category_id'], data['event_category_name'],
                              False)

        try:
            rows_affected = self.sql_helper.execute(query)
            if rows_affected > 0:
                return {'status': 200, 'success': True, 'errors': []}

            return {'status': 500, 'success': False, 'errors': ['Error! Insertion of event_category with id = {} into event_category table unsuccessful'.format(data['event_category_id'])]}
        
        except UniqueViolation:
            return {'status': 400, 'success': False, 'errors': ['Error! event_category with id = {} already exists'.format(data['event_category_id'])]}

    def delete_event_category(self, data):
        query = """ UPDATE \"event_categories\"
                    SET is_deleted = 'true'
                    WHERE event_category_id={}
                """.format(data['event_category_id'])

        rows_affected = self.sql_helper.execute(query)
        
        if rows_affected > 0:
            return {'status': 200, 'success': True, 'errors': []}
        return {'status': 500, 'success': False, 'errors': ['Error! Deletion of event_category with id = {} from event_category table unsuccessful'.format(data['event_category_id'])]}

    def update_event_category(self, data):
        query = """ UPDATE \"event_categories\"
                    SET event_category_name='{}', is_deleted='{}'
                    WHERE event_category_id={}
                """.format(data['event_category_name'], data['is_deleted'],
                           data['event_category_id'])

        rows_affected = self.sql_helper.execute(query)

        if rows_affected > 0:
            return {'status': 200, 'success': True, 'errors': []}
        return {'status': 500, 'success': False, 'errors': ['Error! Updating of event_category with id = {} from event_category table unsuccessful'.format(data['event_category_id'])]}
