from src.service import Service
from src.data.models.user import User
from src.service.helpers.crypto_helper import CryptoHelper
import datetime

class UserService(Service):

    def __init__(self):
        self.user = User()
        self.crypto_helper = CryptoHelper()

    def get_users(self, core_app_context):
        api_response = self.user.get_all_users(core_app_context)

        for row in api_response['data']:
            row.pop('is_deleted', None)
            row.pop('password', None)
        
        return api_response

    def get_user(self, user_id):
        api_response = self.user.get_user(user_id)

        api_response['data'].pop('is_deleted', None)
        api_response['data'].pop('password', None)

        return api_response

    def insert_user(self, data, core_app_context):
        encrypted_password = self.encrypt_password(data)
        data['password'] = encrypted_password
        data['created_on'] = datetime.datetime.now()
        return self.user.insert_user(data, core_app_context)

    def delete_user(self, user_id):
        return self.user.delete_user(user_id)

    def update_user(self, data):
        return self.user.update_user(data)

    def update_profile(self, data, core_app_context):
        return self.user.update_profile(data, core_app_context)

    def change_password(self, data, core_app_context):
        if data['new_password'] != data['confirm_new_password'] or data['old_password'].strip() == '':
            return {'status': 500, 'success': False, 'errors': ['Error! Password changing unsuccessful']}

        user_instance = self.user.sql_helper.get_single_instance('users', 'user_id', core_app_context.user_id)
        data['username'] = user_instance['username']
        data['password'] = data['new_password']
        encrypted_new_password = self.encrypt_password(data)
        data['password'] = encrypted_new_password
        return self.user.change_password(data, core_app_context)

    def encrypt_password(self, data):
        encrypted_password = self.crypto_helper.sha256_encrypt(data['username'], data['password'])
        return encrypted_password

    def update_last_login(self, user_id):        
        return self.user.update_last_login(user_id, datetime.datetime.now())