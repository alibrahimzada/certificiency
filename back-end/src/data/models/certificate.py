from src.data.models.base_entity import BaseEntity
from psycopg2.errors import UniqueViolation

class Certificate(BaseEntity):

    def __init__(self):
        super(Certificate, self).__init__()
   
    def get_all_certificates(self):
        query = """ SELECT *
                    FROM certificates
                    WHERE is_deleted = false
        """
        api_response = {'status': 200, 'success': True, 'errors': []}
        rows = self.sql_helper.get_rows(query, 'certificates')
        api_response['data'] = rows
        return api_response

    def get_certificate(self, certificate_id):
        api_response = {'status': 200, 'success': True, 'errors': []}
        certificate_data = self.sql_helper.get_single_instance('certificates', 'certificate_id', certificate_id)
        api_response['data'] = certificate_data
        return api_response

    def insert_certificate(self, data):
        query = """INSERT INTO \"certificates\" (certificate_id, certified_on, application_id, 
                                 certificate_link, certificate_properties, is_public, is_deleted)
                   values(DEFAULT, '{}', {}, '{}', '{}', '{}', '{}')
                """.format(data['certified_on'], data['application_id'], data['certificate_link'],
                           data['certificate_properties'], data['is_public'], False)

        try:
            rows_affected = self.sql_helper.execute(query)
            if rows_affected > 0:
                return {'status': 200, 'success': True, 'errors': []}

            return {'status': 500, 'success': False, 'errors': ['Error! Insertion of certificate with id = {} into CERTIFICATES table unsuccessful'.format(data['certificate_id'])]}
        
        except UniqueViolation:
            return {'status': 400, 'success': False, 'errors': ['Error! Certificate with id = {} already exists'.format(data['certificate_id'])]}

    def delete_certificate(self, certificate_id):
        query = """ UPDATE \"certificates\"
                    SET is_deleted = 'true'
                    WHERE certificate_id = {}
                """.format(certificate_id)

        rows_affected = self.sql_helper.execute(query)
        
        if rows_affected > 0:
            return {'status': 200, 'success': True, 'errors': []}
        return {'status': 500, 'success': False, 'errors': ['Error while deleting certificate!']}

    def update_certificate(self, data):
        query = """ UPDATE \"certificates\"
                    SET certified_on='{}', certificate_link='{}',
                    certificate_properties='{}', is_public='{}'
                    WHERE certificate_id={}
                """.format(data['certified_on'], data['certificate_link'],
                           data['certificate_properties'], data['is_public'], data['certificate_id'])

        rows_affected = self.sql_helper.execute(query)

        if rows_affected > 0:
            return {'status': 200, 'success': True, 'errors': []}
        return {'status': 500, 'success': False, 'errors': ['Error! Updating of certificate with id = {} from CERTIFICATES table unsuccessful'.format(data['certificate_id'])]}


    def get_my_certificates(self, core_app_context):
        query = """ SELECT * 
                    FROM certificates c
                    WHERE c.application_id IN (
                                        SELECT a.application_id 
                                        FROM applications a
                                        WHERE  a.user_id = {})             
        """.format(core_app_context.user_id)
        
        rows = self.sql_helper.get_rows(query, 'certificates')        

        if len(rows) == 0:
            return {'status': 500, 'success': False, 'errors': ['Error while getting my certificates']}

        return {'status': 200, 'success': True, 'errors': [], 'data': rows}

    def get_event_certificates(self, event_id):
        query = """ SELECT * 
                    FROM certificates c
                    WHERE c.application_id IN (
                                            SELECT a.application_id 
                                            FROM applications a
                                            WHERE a.event_id = {}
                                        )             
                """.format(event_id)

        rows = self.sql_helper.get_rows(query, 'certificates')

        if len(rows) == 0:
            return {'status': 500, 'success': False, 'errors': ['Error while getting event certificates']}

        return {'status': 200, 'success': True, 'errors': [], 'data': rows}
