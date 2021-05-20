from src.data.models.base_entity import BaseEntity
from psycopg2.errors import UniqueViolation

class Auth(BaseEntity):
    def __init__(self):
        super(Auth, self).__init__()

    def login(self, data):
        query = """SELECT * users
                   WHERE username = {} and password = {};
                   """.format(data['username'], data['password'])

        try:
            result = self.sql_helper.query_first_or_default(query)
            if result != None:
                return {'status': 200, 'success': True, 'errors': [], 'data': result}

            return {'status': 500, 'success': False, 'errors': ['Error! Unexpected error, please consult your admin!']}
        
        except UniqueViolation:
            return {'status': 400, 'success': False, 'errors': ['Error! No user found!']}
