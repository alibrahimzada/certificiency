from src.data.models.base_entity import BaseEntity
from psycopg2.errors import UniqueViolation

class Auth(BaseEntity):
    def __init__(self):
        super(Auth, self).__init__()

    def login(self, data):
        query = """ SELECT *
                    FROM users
                    WHERE username = '{}' and password = '{}';
                """.format(data['username'], data['password'])

        try:
            result = self.sql_helper.query_first_or_default(query)
            if result != None:
                result = self.jsonify_result(result)
                return {'status': 200, 'success': True, 'errors': [], 'data': result}

            return {'status': 500, 'success': False, 'errors': ['Error! Unexpected error, please consult your admin!']}
        
        except UniqueViolation:
            return {'status': 400, 'success': False, 'errors': ['Error! No user found!']}

    def jsonify_result(self, result):
        res = {}
        column_names = self.sql_helper.get_column_names('users')

        for i in range(len(result)):
            res[column_names[i][0]] = result[i]

        return res
