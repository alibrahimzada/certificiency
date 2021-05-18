from src.data.models.base_entity import BaseEntity
from psycopg2.errors import UniqueViolation

class Application(BaseEntity):
    def __init__(self):
        super(Application, self).__init__()

    def get_all_applications(self):
        api_response = {'status': 200, 'success': True, 'errors': []}
        rows = self.sql_helper.get_rows('applications')
        api_response['data'] = rows
        return api_response

    def get_application(self, application_id):
        api_response = {'status': 200, 'success': True, 'errors': []}
        application_data = self.sql_helper.get_single_instance('applications', 'application_id', application_id)
        api_response['data'] = application_data
        return api_response

    def insert_application(self, data):
        query = """INSERT INTO \"applications\"
                   values({}, '{}', '{}', '{}', '{}', '{}')
                """.format(data['application_id'], data['event_id'],
                           data['user_id'], data['applied_on'],
                           data['application_status'], False)

        try:
            rows_affected = self.sql_helper.execute(query)
            if rows_affected > 0:
                return {'status': 200, 'success': True, 'errors': []}

            return {'status': 500, 'success': False, 'errors': ['Error! Insertion into APPLICATIONS table unsuccessful']}
        
        except UniqueViolation:
            return {'status': 400, 'success': False, 'errors': ['Error! Application with id = {} already exists'.format(data['application_id'])]}

    def delete_application(self, data):
        query = """UPDATE \"applications\"
                   SET is_deleted = 'true' 
                   WHERE application_id={}
                """.format(data['application_id'])

        rows_affected = self.sql_helper.execute(query)
        
        if rows_affected > 0:
            return {'status': 200, 'success': True, 'errors': []}
        
        return {'status': 500, 'success': False, 'errors': ['Error! Deletion of application with id = {} from APPLICATIONS table unsuccessful'.format(data['application_id'])]}

    def update_application(self, data):
        query = """UPDATE \"applications\"
                   SET event_id='{}', user_id='{}', applied_on='{}', application_status='{}', is_deleted='{}'
                   WHERE application_id={}
                """.format(data['event_id'], data['user_id'], data['applied_on'],
                           data['application_status'], data['is_deleted'], data['application_id'])

        rows_affected = self.sql_helper.execute(query)

        if rows_affected > 0:
            return {'status': 200, 'success': True, 'errors': []}

        return {'status': 500, 'success': False, 'errors': ['Error! Updating of application with id = {} from APPLICATIONS table unsuccessful'.format(data['application_id'])]}
