from src.data.models.base_entity import BaseEntity
from psycopg2.errors import UniqueViolation

class Event(BaseEntity):

    # put variables to init
    def __init__(self):
        super(Event, self).__init__()

    def get_all_events(self):
        query = """ SELECT *
                    FROM events
                    WHERE is_deleted=false
                """

        api_response = {'status': 200, 'success': True, 'errors': []}
        rows = self.sql_helper.get_rows(query, 'events')
        api_response['data'] = rows
        return api_response

    def get_event(self, event_id):
        api_response = {'status': 200, 'success': True, 'errors': []}
        event_data = self.sql_helper.get_single_instance('events', 'event_id', event_id)
        api_response['data'] = event_data
        return api_response

    def insert_event(self, data, core_app_context):
        query = """INSERT INTO \"events\" (event_id, event_name, event_category_id,
                                            event_location, event_thumbnail, event_link,
                                            event_start_date, event_end_date, event_last_application_date,
                                            event_quota, certificate_header, certificate_content, 
                                            customer_id, is_deleted)
                   values(DEFAULT, '{}', {}, '{}', '{}', '{}', '{}', '{}', '{}', {}, '{}', '{}', {}, '{}')
                """.format(data['event_name'], data['event_category_id'],
                           data['event_location'], data['event_thumbnail'], data['event_link'],
                           data['event_start_date'], data['event_end_date'], 
                           data['event_last_application_date'], data['event_quota'],
                           data['certificate_header'], data['certificate_content'],
                           core_app_context.customer_id, False)

        try:
            rows_affected = self.sql_helper.execute(query)
            if rows_affected > 0:
                return {'status': 200, 'success': True, 'errors': []}

            return {'status': 500, 'success': False, 'errors': ['Error! Insertion of event with id = {} into EVENT table unsuccessful'.format(data['event_id'])]}
        
        except UniqueViolation:
            return {'status': 400, 'success': False, 'errors': ['Error! Event with id = {} already exists'.format(data['event_id'])]}

    def delete_event(self, event_id):
        query = """ UPDATE \"events\"
                    SET is_deleted = 'true'
                    WHERE event_id={}
                """.format(event_id)

        rows_affected = self.sql_helper.execute(query)

        if rows_affected > 0:
            return {'status': 200, 'success': True, 'errors': []}
        return {'status': 500, 'success': False, 'errors': ['Error! Deletion of event with id = {} from EVENT table unsuccessful'.format(data['event_id'])]}

    def update_event(self, data):
        query = """ UPDATE \"events\"
                    SET event_name='{}', event_category_id={}, event_location='{}',
                    event_thumbnail='{}', event_link='{}', event_start_date='{}', 
                    event_end_date='{}', event_last_application_date='{}', 
                    event_quota={}, certificate_header = '{}', certificate_content = '{}'
                    WHERE event_id={}
                """.format(data['event_name'], data['event_category_id'], data['event_location'], 
                           data['event_thumbnail'], data['event_link'], data['event_start_date'],
                           data['event_end_date'], data['event_last_application_date'], 
                           data['event_quota'], data['certificate_header'], 
                           data['certificate_content'], data['event_id'])

        rows_affected = self.sql_helper.execute(query)

        if rows_affected > 0:
            return {'status': 200, 'success': True, 'errors': []}
        return {'status': 500, 'success': False, 'errors': ['Error! Updating of event with id = {} from EVENT table unsuccessful'.format(data['event_id'])]}

    def get_my_events(self, core_app_context):
        query = """ SELECT *
                    FROM \"events\"
                    WHERE customer_id={} AND is_deleted=false
                """.format(core_app_context.customer_id)

        rows = self.sql_helper.get_rows(query, 'events')

        if len(rows) == 0:
            return {'status': 500, 'success': False, 'errors': ['Error while getting my events']}

        return {'status': 200, 'success': True, 'errors': [], 'data': rows}

    def get_event_cat_events(self, event_category_id, core_app_context):
        query = """ SELECT *
                    FROM \"events\"
                    WHERE customer_id={} AND is_deleted=false AND event_category_id={}
                """.format(core_app_context.customer_id, event_category_id)

        rows = self.sql_helper.get_rows(query, 'events')

        if len(rows) == 0:
            return {'status': 500, 'success': False, 'errors': ['Error while getting event category events']}

        return {'status': 200, 'success': True, 'errors': [], 'data': rows}
