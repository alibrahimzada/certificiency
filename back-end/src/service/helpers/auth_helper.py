import jwt
import datetime

class IAuthHelper():

    def encode_auth_token(self, user_id, customer_id, role_id):
        pass

class AuthHelper(IAuthHelper):

    def encode_auth_token(self, user_id, customer_id, role_id):
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, minutes=480),
                'iat': datetime.datetime.utcnow(),
                'user_id': user_id,
                'customer_id': customer_id,
                'role_id': role_id
            }

            return jwt.encode(
                payload,
                'certificiency',
                algorithm='HS256'
            )

        except Exception as e:
            return e
