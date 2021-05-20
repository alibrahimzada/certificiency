from src.data.models.base_entity import BaseEntity
from psycopg2.errors import UniqueViolation

class User(BaseEntity):
    def __init__(self):
        super(User, self).__init__()
  
    def get_all_users(self):
        api_response = {'status': 200, 'success': True, 'errors': []}
        rows = self.sql_helper.get_rows('users')
        api_response['data'] = rows
        return api_response

    def get_user(self, user_id):
        api_response = {'status': 200, 'success': True, 'errors': []}
        user_data = self.sql_helper.get_single_instance('users', 'user_id', user_id)
        api_response['data'] = user_data
        return api_response

    def insert_user(self, data):
        query = """INSERT INTO \"users\"
                   values({}, '{}', '{}', '{}', '{}', {}, {}, '{}', '{}', '{}', '{}', '{}');
                   """.format(data['user_id'], data['username'],
                             data['password'], data['first_name'],
                             data['last_name'], data['customer_id'],
                             data['role_id'], data['is_active'],
                             data['email'], data['created_on'],
                             data['last_login'], False)

        try:
            rows_affected = self.sql_helper.execute(query)
            if rows_affected > 0:
                return {'status': 200, 'success': True, 'errors': []}

            return {'status': 500, 'success': False, 'errors': ['Error! Insertion of user with id = {} into USER table unsuccessful'.format(data['user_id'])]}
        
        except UniqueViolation:
            return {'status': 400, 'success': False, 'errors': ['Error! User with id = {} already exists'.format(data['user_id'])]}

    def delete_user(self, data):
        query = """ UPDATE \"users\"
                    SET is_deleted = 'true'
                    WHERE user_id={}
                """.format(data['user_id'])

        rows_affected = self.sql_helper.execute(query)
        
        if rows_affected > 0:
            return {'status': 200, 'success': True, 'errors': []}
        return {'status': 500, 'success': False, 'errors': ['Error! Deletion of user with id = {} from USER table unsuccessful'.format(data['user_id'])]}

    def update_user(self, data):
        query = """ UPDATE \"users\"
                    SET username='{}', password='{}', first_name='{}',
                    last_name='{}', customer_id={}, role_id={}, is_active='{}',
                    email='{}', created_on='{}', last_login='{}', is_deleted='{}'
                    WHERE user_id={}
                """.format(data['username'], data['password'], data['first_name'],
                           data['last_name'], data['customer_id'], data['role_id'], 
                           data['is_active'], data['email'], data['created_on'],
                           data['last_login'], data['is_deleted'], data['user_id'])

        rows_affected = self.sql_helper.execute(query)

        if rows_affected > 0:
            return {'status': 200, 'success': True, 'errors': []}
        return {'status': 500, 'success': False, 'errors': ['Error! Updating of user with id = {} from USER table unsuccessful'.format(data['user_id'])]}
