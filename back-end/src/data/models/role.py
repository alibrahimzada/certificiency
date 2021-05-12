from data.models.base_entity import BaseEntity
from psycopg2.errors import UniqueViolation

class Role(BaseEntity):
    def __init__(self):
        super(Role, self).__init__()
  
    def get_all_roles(self):
        api_response = {'status': 200, 'success': True, 'errors': []}
        rows = self.sql_helper.get_rows('roles')
        api_response['data'] = rows
        return api_response

    def insert_role(self, data):
        query = """INSERT INTO \"roles\"
                   values({}, '{}', '{}', '{}', '{}');
                   """.format(data['role_id'], data['role_name'],
                             data['role_permissions'], data['customer_id'],
                             False)

        try:
            rows_affected = self.sql_helper.execute(query)
            if rows_affected > 0:
                return {'status': 200, 'success': True, 'errors': []}

            return {'status': 500, 'success': False, 'errors': ['Error! Insertion of role with id = {} into ROLE table unsuccessful'.format(data['role_id'])]}
        
        except UniqueViolation:
            return {'status': 400, 'success': False, 'errors': ['Error! Role with id = {} already exists'.format(data['role_id'])]}

    def delete_role(self, data):
        query = """ DELETE FROM \"roles\"
                    WHERE role_id={}
                """.format(data['role_id'])

        rows_affected = self.sql_helper.execute(query)
        
        if rows_affected > 0:
            return {'status': 200, 'success': True, 'errors': []}
        return {'status': 500, 'success': False, 'errors': ['Error! Deletion of role with id = {} from ROLE table unsuccessful'.format(data['role_id'])]}

    def update_role(self, data):
        query = """ UPDATE \"roles\"
                    SET role_name='{}', role_permissions='{}', customer_id='{}'
                    WHERE role_id={}
                """.format(data['role_name'], data['role_permissions'],
                            data['customer_id'], data['role_id'])

        rows_affected = self.sql_helper.execute(query)

        if rows_affected > 0:
            return {'status': 200, 'success': True, 'errors': []}
        return {'status': 500, 'success': False, 'errors': ['Error! Updating of role with id = {} from ROLE table unsuccessful'.format(data['role_id'])]}