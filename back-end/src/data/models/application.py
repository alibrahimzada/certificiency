from src.data.models.base_entity import BaseEntity
from psycopg2.errors import UniqueViolation

class Application(BaseEntity):
    def __init__(self):
        super(Application, self).__init__()

    def get_all_applications(self, core_app_context):
        query = """ SELECT * 
                    FROM \"applications\"
                    WHERE user_id = {} AND is_deleted = false
        """.format(core_app_context.user_id)
        api_response = {'status': 200, 'success': True, 'errors': []}
        rows = self.sql_helper.get_rows(query, 'applications')
        api_response['data'] = rows
        return api_response

    def get_application(self, application_id):
        api_response = {'status': 200, 'success': True, 'errors': []}
        application_data = self.sql_helper.get_single_instance('applications', 'application_id', application_id)
        api_response['data'] = application_data
        return api_response

    def insert_application(self, data, core_app_context):
        query = """INSERT INTO \"applications\" (application_id, event_id,
                                 user_id, applied_on, application_status, is_deleted)
                   values(DEFAULT, '{}', '{}', '{}', '{}', '{}')
                """.format(data['event_id'], core_app_context.user_id, 
                           data['applied_on'], 0, False)
        try:
            rows_affected = self.sql_helper.execute(query)
            if rows_affected > 0:
                return {'status': 200, 'success': True, 'errors': []}

            return {'status': 500, 'success': False, 'errors': ['Error! Insertion into APPLICATIONS table unsuccessful']}
        
        except UniqueViolation:
            return {'status': 400, 'success': False, 'errors': ['Error! Application with id = {} already exists'.format(data['application_id'])]}

    def delete_application(self, application_id):
        query = """UPDATE \"applications\"
                   SET is_deleted = 'true' 
                   WHERE application_id={}
                """.format(application_id)

        rows_affected = self.sql_helper.execute(query)
        
        if rows_affected > 0:
            return {'status': 200, 'success': True, 'errors': []}
        
        return {'status': 500, 'success': False, 'errors': ['Error while deleting application!']}

    def update_application(self, data):
        query = """UPDATE \"applications\"
                   SET application_status='{}'
                   WHERE application_id = {}
                """.format(data['application_status'], data['application_id'])

        rows_affected = self.sql_helper.execute(query)

        if rows_affected > 0:
            return {'status': 200, 'success': True, 'errors': []}

        return {'status': 500, 'success': False, 'errors': ['Error! Updating of application with id = {} from APPLICATIONS table unsuccessful'.format(data['application_id'])]}

    def update_application_status(self, data):
        query = """UPDATE applications
                   SET application_status = '{}'  
                   WHERE application_id = {} 

        """.format(data['application_status'], data['application_id'])
        
        rows_affected = self.sql_helper.execute(query)

        if rows_affected > 0:
            return {'status': 200, 'success': True, 'errors': []}

        return {'status': 500, 'success': False, 'errors': ['Error while udpating application status!']}

    def get_event_applications(self, event_id, core_app_context):
        query = """SELECT *
                   FROM \"applications\"
                   WHERE user_id={} AND is_deleted=false AND event_id={}
                """.format(core_app_context.user_id, event_id)

        rows = self.sql_helper.get_rows(query, 'applications')

        if len(rows) == 0:
            return {'status': 500, 'success': False, 'errors': ['Error while getting event applications']}

        return {'status': 200, 'success': True, 'errors': [], 'data': rows}

    def is_application_available(self, data, core_app_context):
        query = """ SELECT *
                    FROM applications
                    WHERE user_id = {} AND event_id = {}
        """.format(core_app_context.user_id, data['event_id'])
        
        result = self.sql_helper.query_first_or_default(query)

        if result == None:
            return False
        return True

    def is_quota_available(self, data):
        query = """ SELECT COUNT(a.application_id)
                    FROM applications a, events e
                    WHERE e.event_id = {} AND
                    a.event_id = e.event_id
                """.format(data['event_id'])

        result = self.sql_helper.query_first_or_default(query)
        total_applications = result[0]

        query = """ SELECT e.event_quota
                    FROM events e
                    WHERE e.event_id = {} 
        """.format(data['event_id'])

        result = self.sql_helper.query_first_or_default(query)
        total_quota = result[0]

        if total_applications < total_quota:
            return True
        return False
