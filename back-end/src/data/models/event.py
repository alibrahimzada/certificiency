from data.models.base_entity import BaseEntity
from psycopg2.errors import UniqueViolation

class Event(BaseEntity):

    # put variables to init
    def __init__(self):
        super(Event, self).__init__()

    def get_all_events(self):
        api_response = {'status': 200, 'success': True, 'errors': []}
        rows = self.sql_helper.get_rows('events')
        api_response['data'] = rows
        return api_response

    def get_event(self, event_id):
        api_response = {'status': 200, 'success': True, 'errors': []}
        event_data = self.sql_helper.get_single_instance('events', 'event_id', event_id)
        api_response['data'] = event_data
        return api_response

    def insert_event(self, data):
        query = """INSERT INTO \"events\"
                   values({}, '{}', {}, '{}', '{}', '{}', '{}')
                """.format(data['event_id'], data['event_name'], data['event_category_id'],
                           data['event_location'], data['event_thumbnail'], data['event_link'],
                           False)

        try:
            rows_affected = self.sql_helper.execute(query)
            if rows_affected > 0:
                return {'status': 200, 'success': True, 'errors': []}

            return {'status': 500, 'success': False, 'errors': ['Error! Insertion of event with id = {} into EVENT table unsuccessful'.format(data['event_id'])]}
        
        except UniqueViolation:
            return {'status': 400, 'success': False, 'errors': ['Error! Event with id = {} already exists'.format(data['event_id'])]}

    def delete_event(self, data):
        query = """ UPDATE \"events\"
                    SET is_deleted = 'true'
                    WHERE event_id={}
                """.format(data['event_id'])

        rows_affected = self.sql_helper.execute(query)

        if rows_affected > 0:
            return {'status': 200, 'success': True, 'errors': []}
        return {'status': 500, 'success': False, 'errors': ['Error! Deletion of event with id = {} from EVENT table unsuccessful'.format(data['event_id'])]}

    def update_event(self, data):
        query = """ UPDATE \"events\"
                    SET event_name='{}', event_category_id={}, event_location='{}',
                    event_thumbnail='{}', event_link='{}', is_deleted='{}'
                    WHERE event_id={}
                """.format(data['event_name'], data['event_category_id'], data['event_location'], 
                           data['event_thumbnail'], data['event_link'], data['is_deleted'],
                           data['event_id'])

        rows_affected = self.sql_helper.execute(query)

        if rows_affected > 0:
            return {'status': 200, 'success': True, 'errors': []}
        return {'status': 500, 'success': False, 'errors': ['Error! Updating of event with id = {} from EVENT table unsuccessful'.format(data['event_id'])]}
