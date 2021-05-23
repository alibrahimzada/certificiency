from src.data.models.base_entity import BaseEntity
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
                           False)

        try:
            rows_affected = self.sql_helper.execute(query)
            if rows_affected > 0:
                return {'status': 200, 'success': True, 'errors': []}

            return {'status': 500, 'success': False, 'errors': ['Error! Insertion of certificate with id = {} into CERTIFICATES table unsuccessful'.format(data['certificate_id'])]}
        
        except UniqueViolation:
            return {'status': 400, 'success': False, 'errors': ['Error! Certificate with id = {} already exists'.format(data['certificate_id'])]}

    def delete_certificate(self, data):
        query = """ UPDATE \"certificates\"
                    SET is_deleted = 'true'
                    WHERE certificate_id={}
                """.format(data['certificate_id'])

        rows_affected = self.sql_helper.execute(query)
        
        if rows_affected > 0:
            return {'status': 200, 'success': True, 'errors': []}
        return {'status': 500, 'success': False, 'errors': ['Error! Deletion of certificate with id = {} from CERTIFICATES table unsuccessful'.format(data['certificate_id'])]}

    def update_certificate(self, data):
        query = """ UPDATE \"certificates\"
                    SET certified_on='{}', application_id='{}', certificate_link='{}',
                    certificate_properties='{}', is_public='{}', is_deleted='{}'
                    WHERE certificate_id={}
                """.format(data['certified_on'], data['application_id'], data['certificate_link'],
                           data['certificate_properties'], data['is_public'], data['is_deleted'],
                           data['certificate_id'])

        rows_affected = self.sql_helper.execute(query)

        if rows_affected > 0:
            return {'status': 200, 'success': True, 'errors': []}
        return {'status': 500, 'success': False, 'errors': ['Error! Updating of certificate with id = {} from CERTIFICATES table unsuccessful'.format(data['certificate_id'])]}


    def get_my_certificates(self, core_app_context):

        query = """
            SELECT c.certificate_id, c.certified_on, c.application_id, c.certificate_link, c.certificate_properties, c.is_public, c.is_deleted 
            FROM certificates c, applications a
            WHERE c.application_id = a.application_id AND
                  a.user_id = {}          
        """.format(core_app_context.user_id)

        result = self.sql_helper.query_all(query)
        if len(result) == 0:
            return {'status': 500, 'success': False, 'errors': ['Error while getting certificates']}

        column_names = self.sql_helper.get_column_names('certificates')
        my_certificates = []
        for certificate in result:
            certificate_data = {}
            for i in range(len(certificate)):
                certificate_data[column_names[i][0]] = certificate[i]
            my_certificates.append(certificate_data)
   

        return {'status': 200, 'success': True, 'errors': [], 'data': my_certificates}
