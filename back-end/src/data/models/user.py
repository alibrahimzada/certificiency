from src.data.models.base_entity import BaseEntity
from psycopg2.errors import UniqueViolation

class User(BaseEntity):
    def __init__(self):
        super(User, self).__init__()
  
    def get_all_users(self, core_app_context):
        query = """ SELECT *
                    FROM users
                    WHERE customer_id={} AND is_deleted=false
                """.format(core_app_context.customer_id)
        
        rows = self.sql_helper.get_rows(query, 'users')
        if len(rows) == 0:
            return {'status': 500, 'success': False, 'errors': ['Error while getting all users!']}

        return {'status': 200, 'success': True, 'errors': [], 'data': rows}

    def get_user(self, user_id):
        api_response = {'status': 200, 'success': True, 'errors': []}
        user_data = self.sql_helper.get_single_instance('users', 'user_id', user_id)
        api_response['data'] = user_data
        return api_response

    def insert_user(self, data, core_app_context):
        query = """INSERT INTO \"users\" (user_id, username, password, first_name, last_name, 
                                          customer_id, role_id, user_type, 
                                          is_active, email, created_on, last_login, is_deleted)
                   values(DEFAULT, '{}', '{}', '{}', '{}', {}, {}, {}, '{}', '{}', '{}', '{}', '{}');
                   """.format(data['username'],
                             data['password'], data['first_name'],
                             data['last_name'], core_app_context.customer_id,
                             data['role_id'], data['user_type'], True,
                             data['email'], data['created_on'],
                             data['created_on'], False)

        try:
            rows_affected = self.sql_helper.execute(query)
            if rows_affected > 0:
                return {'status': 200, 'success': True, 'errors': []}

            return {'status': 500, 'success': False, 'errors': ['Error! Insertion of user with id = {} into USER table unsuccessful'.format(data['user_id'])]}
        
        except UniqueViolation:
            return {'status': 400, 'success': False, 'errors': ['Error! User with id = {} already exists'.format(data['user_id'])]}

    def delete_user(self, user_id):
        query = """ UPDATE \"users\"
                    SET is_deleted = 'true'
                    WHERE user_id={}
                """.format(user_id)

        rows_affected = self.sql_helper.execute(query)
        
        if rows_affected > 0:
            return {'status': 200, 'success': True, 'errors': []}
        return {'status': 500, 'success': False, 'errors': ['Error! Deletion unsuccessful']}

    def update_user(self, data):
        query = """ UPDATE \"users\"
                    SET username='{}', first_name='{}', last_name='{}',
                    role_id={}, user_type={}, is_active='{}', email='{}'
                    WHERE user_id={}
                """.format(data['username'], data['first_name'], data['last_name'],
                           data['role_id'],  data['user_type'], data['is_active'], data['email'], data['user_id'])

        rows_affected = self.sql_helper.execute(query)

        if rows_affected > 0:
            return {'status': 200, 'success': True, 'errors': []}
        return {'status': 500, 'success': False, 'errors': ['Error! Updating of user with id = {} from USER table unsuccessful'.format(data['user_id'])]}

    def update_profile(self, data, core_app_context):
        query = """ UPDATE \"users\"
                    SET first_name='{}', last_name='{}', email='{}'
                    WHERE user_id={}
                """.format(data['first_name'], data['last_name'], data['email'], core_app_context.user_id)

        rows_affected = self.sql_helper.execute(query)

        if rows_affected > 0:
            return {'status': 200, 'success': True, 'errors': []}
        return {'status': 500, 'success': False, 'errors': ['Error! Updating user profile unsuccessful']}

    def change_password(self, data, core_app_context):
        query = """ UPDATE \"users\"
                    SET password = '{}'
                    WHERE user_id={}
                """.format(data['password'], core_app_context.user_id)

        rows_affected = self.sql_helper.execute(query)

        if rows_affected > 0:
            return {'status': 200, 'success': True, 'errors': []}
        return {'status': 500, 'success': False, 'errors': ['Error! Changing password unsuccessful']}


    def update_last_login(self, user_id, last_login_datetime):
        query = """ UPDATE users
                    SET last_login = '{}'
                    WHERE user_id = {}
        """.format(last_login_datetime, user_id)
        rows_affected = self.sql_helper.execute(query)

        if rows_affected > 0:
            return {'status': 200, 'success': True, 'errors': []}
        return {'status': 500, 'success': False, 'errors': ['Error! Updating last login unsuccessful']}
