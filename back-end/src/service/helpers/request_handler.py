import jwt
import datetime

class CoreAppContext():

    def __init__(self, user_id, customer_id, role_id):
        self.user_id = user_id
        self.customer_id = customer_id
        self.role_id = role_id

class RequestHandler():

    def __init__(self, request=None):
        self.request = request

    def validate_token(self, request):
        self.request = request
        token = request.headers.get('Authorization')
        token = token.split(' ')[1]

        res = self.decode_token(token)

        if res != None:
            return {'status': 200, 'success': True, 'errors': [], 'core_app_context': res}

        return {'status': 400, 'success': False, 'errors': ['Error! Token has been expired.']}

    def decode_token(self, jwt_token):
        decoded_token = jwt.decode(jwt_token, 'certificiency', algorithms=["HS256"])

        if self.is_expired(decoded_token['exp']):
            core_app_context = CoreAppContext(decoded_token['user_id'],
                                              decoded_token['customer_id'],
                                              decoded_token['role_id'])

            return core_app_context

        return None

    def is_expired(self, exp):
        exp_datetime = datetime.datetime.fromtimestamp(exp)

        if exp_datetime > datetime.datetime.now():
            return True

        return False
