from data.models.base_entity import BaseEntity
from psycopg2.errors import UniqueViolation

class Certificate(BaseEntity):

    def __init__(self):
        super(Certificate, self).__init__()
   
    def get_all_certificates(self):
        api_response = {'status': 200, 'success': True, 'errors': []}
        rows = self.sql_helper.get_rows('certificates')
        api_response['data'] = rows
        return api_response

    def get_certificate(self, certificate_id):
        api_response = {'status': 200, 'success': True, 'errors': []}
        certificate_data = self.sql_helper.get_single_instance('certificates', 'certificate_id', certificate_id)
        api_response['data'] = certificate_data
        return api_response

    def insert_certificate(self, data):
        query = """INSERT INTO \"certificates\"
                   values({}, '{}', {}, '{}', '{}', '{}', '{}')
                """.format(data['certificate_id'], data['certified_on'],
                           data['application_id'], data['certificate_link'],
                           data['certificate_properties'], data['is_public'],
                           data['is_active'])

        try:
            rows_affected = self.sql_helper.execute(query)
            if rows_affected > 0:
                return {'status': 200, 'success': True, 'errors': []}

            return {'status': 500, 'success': False, 'errors': ['Error! Insertion of certificate with id = {} into CERTIFICATES table unsuccessful'.format(data['certificate_id'])]}
        
        except UniqueViolation:
            return {'status': 400, 'success': False, 'errors': ['Error! Certificate with id = {} already exists'.format(data['certificate_id'])]}

    def delete_certificate(self, data):
        query = """ DELETE FROM \"certificates\"
                    WHERE certificate_id={}
                """.format(data['certificate_id'])

        rows_affected = self.sql_helper.execute(query)
        
        if rows_affected > 0:
            return {'status': 200, 'success': True, 'errors': []}
        return {'status': 500, 'success': False, 'errors': ['Error! Deletion of certificate with id = {} from CERTIFICATES table unsuccessful'.format(data['certificate_id'])]}

    def update_certificate(self, data):
        query = """ UPDATE \"certificates\"
                    SET certified_on='{}', application_id='{}', certification_link='{}',
                    certificate_properties='{}', is_public='{}', is_active='{}'
                    WHERE certificate_id={}
                """.format(data['certified_on'], data['application_id'], data['certificate_link'],
                           data['certificate_properties'], data['is_public'], data['is_active'],
                           data['certificate_id'])

        rows_affected = self.sql_helper.execute(query)

        if rows_affected > 0:
            return {'status': 200, 'success': True, 'errors': []}
        return {'status': 500, 'success': False, 'errors': ['Error! Updating of certificate with id = {} from CERTIFICATES table unsuccessful'.format(data['certificate_id'])]}
